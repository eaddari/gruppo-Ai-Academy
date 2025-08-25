import httpx
import streamlit as st
import os
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path

from langchain.schema import Document
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# LangChain Core (prompt/chain)
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from dotenv import load_dotenv


# =========================
# Configurazione
# =========================


@dataclass
class Settings:
    # Persistenza FAISS
    persist_dir: str = "faiss_index_streamlit"
    # Text splitting
    chunk_size: int = 1000
    chunk_overlap: int = 200
    # Retriever (MMR)
    search_type: str = "mmr"  # "mmr" o "similarity"
    k: int = 3  # risultati finali
    fetch_k: int = 20  # candidati iniziali (per MMR)
    mmr_lambda: float = 0.3  # 0 = diversificazione massima, 1 = pertinenza massima


httpx_client = httpx.Client(http2=True, verify=False)


def setup_azure_openai():
    """
    Configura Azure OpenAI con le variabili d'ambiente.
    """
    # Carica le variabili dal file .env
    load_dotenv(dotenv_path=".env")

    # Recupera le variabili di ambiente
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment_chat = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME_CHAT")
    deployment_embedding = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME_EMBEDDING")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")

    if not all([api_key, endpoint, deployment_chat, deployment_embedding, api_version]):
        st.error(
            "⚠️ Assicurati che tutte le variabili di ambiente Azure OpenAI siano configurate nel file .env"
        )
        st.stop()

    llm = AzureChatOpenAI(
        http_client=httpx_client,
        azure_endpoint=endpoint,
        azure_deployment=deployment_chat,
        api_version=api_version,
    )

    embeddings = AzureOpenAIEmbeddings(
        http_client=httpx_client,
        azure_endpoint=endpoint,
        azure_deployment=deployment_embedding,
        api_version=api_version,
    )

    return llm, embeddings


# =========================
# Funzioni di utilità per documenti
# =========================


def load_uploaded_file(uploaded_file) -> list[Document]:
    """
    Carica un file caricato dall'utente e lo converte in documenti LangChain.
    """
    documents = []

    # Salva temporaneamente il file
    with tempfile.NamedTemporaryFile(
        delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}"
    ) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    try:
        if uploaded_file.name.lower().endswith(".pdf"):
            loader = PyPDFLoader(tmp_path)
            documents = loader.load()
            # Sovrascrive il metadata source con il nome originale del file
            for doc in documents:
                doc.metadata["source"] = uploaded_file.name
        elif uploaded_file.name.lower().endswith((".txt", ".md")):
            # Leggi il contenuto come testo
            content = uploaded_file.getvalue().decode("utf-8")

            if uploaded_file.name.lower().endswith(".md") and "---" in content:
                # Split usando regex per i trattini (come nel codice originale)
                blocks = re.split(r"\n\s*---\s*\n", content.strip())

                for i, block in enumerate(blocks):
                    cleaned_block = block.strip()
                    if cleaned_block:
                        doc = Document(
                            page_content=cleaned_block,
                            metadata={
                                "source": f"{uploaded_file.name}_section_{i + 1}",
                                "file_path": uploaded_file.name,
                                "section_number": i + 1,
                            },
                        )
                        documents.append(doc)
            else:
                # File di testo normale
                doc = Document(
                    page_content=content,
                    metadata={
                        "source": uploaded_file.name,
                        "file_path": uploaded_file.name,
                    },
                )
                documents.append(doc)
        else:
            st.error(f"Tipo di file non supportato: {uploaded_file.name}")
            return []

    finally:
        # Pulisci il file temporaneo
        os.unlink(tmp_path)

    return documents


def split_documents(docs: list[Document], settings: Settings) -> list[Document]:
    """
    Applica uno splitting robusto ai documenti per ottimizzare il retrieval.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            "; ",
            ": ",
            ", ",
            " ",
            "",  # fallback aggressivo
        ],
    )
    return splitter.split_documents(docs)


def build_faiss_vectorstore(
    chunks: list[Document], embeddings_func: AzureOpenAIEmbeddings, persist_dir: str
) -> FAISS:
    """
    Costruisce da zero un FAISS index e lo salva su disco.
    """
    vs = FAISS.from_documents(documents=chunks, embedding=embeddings_func)

    Path(persist_dir).mkdir(parents=True, exist_ok=True)
    vs.save_local(persist_dir)
    return vs


def make_retriever(vector_store: FAISS, settings: Settings):
    """
    Configura il retriever. Con 'mmr' otteniamo risultati meno ridondanti e più coprenti.
    """
    if settings.search_type == "mmr":
        return vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": settings.k,
                "fetch_k": settings.fetch_k,
                "lambda_mult": settings.mmr_lambda,
            },
        )
    else:
        return vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": settings.k},
        )


def format_docs_for_prompt(docs: list[Document]) -> str:
    """
    Prepara il contesto per il prompt, includendo citazioni [source].
    """
    lines = []
    for i, d in enumerate(docs, start=1):
        src = d.metadata.get("source", f"doc{i}")
        # Estrai solo il nome del file dal percorso completo
        src = os.path.basename(src) if src else f"doc{i}"
        section = d.metadata.get("section_number", "")
        section_info = f" (sezione {section})" if section else ""
        lines.append(f"[source:{src}{section_info}] {d.page_content}")
    return "\n\n".join(lines)


def build_rag_chain(llm_model, retriever):
    """
    Costruisce la catena RAG (retrieval -> prompt -> LLM) con citazioni e regole anti-hallucination.
    """
    system_prompt = (
        "Sei un assistente esperto che risponde a domande basandoti sul corpus di documenti fornito. "
        "Rispondi in italiano basandoti esclusivamente sul CONTENUTO fornito nel contesto. "
        "Se l'informazione non è presente nel contesto, dichiara che non è disponibile. "
        "Includi sempre citazioni precise nel formato [source:...]. "
        "Sii accurato e preciso nelle risposte."
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            (
                "human",
                "Domanda:\n{question}\n\n"
                "Contesto (estratti dal corpus):\n{context}\n\n"
                "Istruzioni:\n"
                "1) Rispondi solo con informazioni contenute nel contesto.\n"
                "2) Cita sempre le fonti pertinenti nel formato [source:...].\n"
                "3) Se la risposta non è nel contesto, scrivi: 'Non è presente nel contesto fornito.'",
            ),
        ]
    )

    # LCEL: dict -> prompt -> llm -> parser
    chain = (
        {
            "context": retriever | format_docs_for_prompt,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm_model
        | StrOutputParser()
    )
    return chain


# =========================
# Funzioni Streamlit
# =========================


def initialize_session_state():
    """Inizializza le variabili di stato della sessione."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "rag_chain" not in st.session_state:
        st.session_state.rag_chain = None
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None
    if "documents_loaded" not in st.session_state:
        st.session_state.documents_loaded = False


def sidebar_config():
    """Configura la sidebar per il caricamento documenti e parametri RAG."""
    st.sidebar.title("🔧 Configurazione RAG")

    # Sezione caricamento documenti
    st.sidebar.header("📁 Carica Documenti")
    uploaded_files = st.sidebar.file_uploader(
        "Scegli file (PDF, TXT, MD)",
        type=["pdf", "txt", "md"],
        accept_multiple_files=True,
        help="Carica uno o più documenti per alimentare il sistema RAG",
    )

    # Parametri RAG
    st.sidebar.header("⚙️ Parametri RAG")

    col1, col2 = st.sidebar.columns(2)
    with col1:
        chunk_size = st.number_input(
            "Chunk Size",
            min_value=100,
            max_value=2000,
            value=1000,
            step=100,
            help="Dimensione dei chunk di testo",
        )
    with col2:
        chunk_overlap = st.number_input(
            "Chunk Overlap",
            min_value=0,
            max_value=500,
            value=200,
            step=50,
            help="Sovrapposizione tra i chunk",
        )

    search_type = st.sidebar.selectbox(
        "Tipo di Ricerca",
        ["mmr", "similarity"],
        index=0,
        help="MMR bilancia rilevanza e diversità",
    )

    col3, col4 = st.sidebar.columns(2)
    with col3:
        k = st.number_input(
            "Risultati finali (k)",
            min_value=1,
            max_value=10,
            value=3,
            step=1,
            help="Numero di documenti da recuperare",
        )
    with col4:
        fetch_k = st.number_input(
            "Candidati iniziali",
            min_value=5,
            max_value=50,
            value=20,
            step=5,
            help="Candidati per MMR (solo se MMR attivo)",
        )

    mmr_lambda = st.sidebar.slider(
        "MMR Lambda",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.1,
        help="0 = max diversità, 1 = max rilevanza",
    )

    # Pulsante per processare i documenti
    process_docs = st.sidebar.button("🚀 Processa Documenti", type="primary")

    settings = Settings(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        search_type=search_type,
        k=k,
        fetch_k=fetch_k,
        mmr_lambda=mmr_lambda,
    )

    return uploaded_files, settings, process_docs


def process_documents(uploaded_files, settings):
    """Processa i documenti caricati e costruisce il vector store."""
    if not uploaded_files:
        st.sidebar.error("❌ Nessun file caricato!")
        return False

    with st.sidebar:
        with st.spinner("🔄 Processando documenti..."):
            try:
                # Configura Azure OpenAI
                llm, embeddings = setup_azure_openai()

                # Carica tutti i documenti
                all_documents = []
                for uploaded_file in uploaded_files:
                    docs = load_uploaded_file(uploaded_file)
                    all_documents.extend(docs)

                if not all_documents:
                    st.error("❌ Nessun documento valido caricato!")
                    return False

                # Split dei documenti
                chunks = split_documents(all_documents, settings)

                # Costruisci vector store
                vector_store = build_faiss_vectorstore(
                    chunks, embeddings, settings.persist_dir
                )

                # Crea retriever e chain
                retriever = make_retriever(vector_store, settings)
                rag_chain = build_rag_chain(llm, retriever)

                # Salva nello stato della sessione
                st.session_state.vector_store = vector_store
                st.session_state.rag_chain = rag_chain
                st.session_state.documents_loaded = True

                st.success(
                    f"✅ Processati {len(all_documents)} documenti in {len(chunks)} chunks!"
                )
                return True

            except Exception as e:
                st.error(f"❌ Errore durante il processamento: {str(e)}")
                return False


def display_chat():
    """Mostra l'interfaccia chat principale."""
    st.title("🤖 Chat RAG System")

    if not st.session_state.documents_loaded:
        st.info("👈 Carica dei documenti nella sidebar per iniziare!")
        return

    # Mostra cronologia chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input utente
    if prompt := st.chat_input("Fai una domanda sui documenti caricati..."):
        # Aggiungi messaggio utente
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Genera risposta
        with st.chat_message("assistant"):
            with st.spinner("🤔 Sto pensando..."):
                try:
                    response = st.session_state.rag_chain.invoke(prompt)
                    st.markdown(response)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response}
                    )
                except Exception as e:
                    error_msg = (
                        f"❌ Errore durante la generazione della risposta: {str(e)}"
                    )
                    st.error(error_msg)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": error_msg}
                    )


def main():
    """Funzione principale dell'app Streamlit."""
    st.set_page_config(
        page_title="RAG Chat System",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Inizializza stato sessione
    initialize_session_state()

    # Configura sidebar
    uploaded_files, settings, process_docs = sidebar_config()

    # Processa documenti se richiesto
    if process_docs:
        process_documents(uploaded_files, settings)

    # Mostra chat principale
    display_chat()

    # Footer nella sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("**💡 Come usare:**")
    st.sidebar.markdown("1. Carica documenti (PDF, TXT, MD)")
    st.sidebar.markdown("2. Modifica parametri se necessario")
    st.sidebar.markdown("3. Clicca 'Processa Documenti'")
    st.sidebar.markdown("4. Inizia a chattare!")


if __name__ == "__main__":
    main()
