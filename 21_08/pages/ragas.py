import streamlit as st
import sys
from pathlib import Path

# Add parent directory to import from rag_app
sys.path.append(str(Path(__file__).parent.parent))

from chat import setup_azure_openai, Settings, make_retriever

try:
    import ragas
    from ragas.metrics import (
        context_precision,
        context_recall,
        faithfulness,
        answer_relevancy,
        answer_correctness,
    )
    from ragas import EvaluationDataset
except ImportError:
    st.error("Please install ragas: pip install ragas")
    st.stop()

st.set_page_config(page_title="Ragas Metrics", layout="wide")

st.title("🧪 Ragas Metrics")

# Initialize session state
if "evaluation_results" not in st.session_state:
    st.session_state.evaluation_results = None


def build_ragas_dataset(questions, retriever, chain, ground_truth=None):
    dataset = []
    for question in questions:
        retrieved_docs = retriever.invoke(question)
        contexts = [doc.page_content for doc in retrieved_docs]
        answer = chain.invoke(question)

        entry = {"question": question, "contexts": contexts, "answer": answer}
        if ground_truth and question in ground_truth and ground_truth[question]:
            entry["reference"] = ground_truth[question]
        dataset.append(entry)
    return dataset


# Setup
try:
    llm, embeddings = setup_azure_openai()
except Exception as e:
    st.error(f"❌ Error configuring Azure OpenAI: {str(e)}")
    st.stop()

# Check RAG system
if "rag_chain" not in st.session_state or "vector_store" not in st.session_state:
    st.warning("⚠️ Load documents in the main app first.")
    st.stop()

rag_chain = st.session_state.rag_chain
retriever = make_retriever(st.session_state.vector_store, Settings())

# Questions
st.header("📝 Questions")
questions = []
for i in range(3):
    q = st.text_input(f"Question {i + 1}:", key=f"q_{i}")
    if q.strip():
        questions.append(q.strip())

# Ground truth (optional)
st.header("🎯 Ground Truth (Optional)")
ground_truth = {}
for i, question in enumerate(questions):
    gt = st.text_area(f"Expected answer {i + 1}:", key=f"gt_{i}", height=80)
    if gt.strip():
        ground_truth[question] = gt.strip()

# Evaluation
if st.button("🚀 Run Evaluation") and questions:
    with st.spinner("Running evaluation..."):
        try:
            dataset = build_ragas_dataset(questions, retriever, rag_chain, ground_truth)
            evaluation_dataset = EvaluationDataset.from_list(dataset)

            metrics = [
                context_precision,
                context_recall,
                faithfulness,
                answer_relevancy,
            ]
            if all("reference" in row for row in dataset):
                metrics.append(answer_correctness)

            ragas_result = ragas.evaluate(
                dataset=evaluation_dataset,
                metrics=metrics,
                llm=llm,
                embeddings=embeddings,
            )

            st.session_state.evaluation_results = ragas_result.to_pandas()
            st.success("✅ Evaluation completed!")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Results
if st.session_state.evaluation_results is not None:
    st.header("📊 Results")
    df = st.session_state.evaluation_results

    # Metrics
    cols = st.columns(
        len(
            [
                col
                for col in df.columns
                if col not in ["question", "answer", "contexts", "reference"]
            ]
        )
    )
    for i, col in enumerate(
        [
            c
            for c in df.columns
            if c not in ["question", "answer", "contexts", "reference"]
        ]
    ):
        with cols[i]:
            st.metric(col.replace("_", " ").title(), f"{df[col].mean():.3f}")

    # Table
    st.dataframe(df, use_container_width=True)

    # Download
    st.download_button(
        "📥 Download CSV", df.to_csv(index=False), "ragas_results.csv", "text/csv"
    )
