from src.esercizio_esteso.crews.rag.faiss_rag import extract_sphinx_docs, corpus
from pathlib import Path

# Test extract_sphinx_docs
sphinx_dir = Path('docs/build/html')
print(f"Sphinx dir exists: {sphinx_dir.exists()}")

if sphinx_dir.exists():
    docs = extract_sphinx_docs(sphinx_dir)
    print(f"Sphinx docs found: {len(docs)}")
    for doc in docs[:3]:
        print(f"- {doc['source']}: {len(doc['content'])} chars")

# Test corpus
print("\nTesting corpus function:")
all_docs = corpus()
print(f"Total documents: {len(all_docs)}")
for doc in all_docs:
    print(f"- {doc.metadata}")
