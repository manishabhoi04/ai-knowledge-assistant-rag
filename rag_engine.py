import chromadb
import requests

from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("BAAI/bge-small-en-v1.5")

# Connect to ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection_metadata = client.get_or_create_collection(
    name="ml_handbook_metadata"
)

# Debug
print("Collection Count:", collection_metadata.count())


def ask_rag_with_sources(question):

    # Create query embedding
    query_embedding = model.encode(question)

    # Search ChromaDB
    results = collection_metadata.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3
    )

    retrieved_chunks = results["documents"][0]
    retrieved_metadata = results["metadatas"][0]

    # Debug
    print("\nRetrieved Chunks:")
    print(retrieved_chunks)

    print("\nRetrieved Metadata:")
    print(retrieved_metadata)

    # Build context
    context = "\n\n".join(retrieved_chunks)

    print("\nContext Length:", len(context))

    # Build prompt
    prompt = f"""
You are a helpful assistant.

Use the provided context to answer the question.

If the answer exists in the context, explain it in 3-5 sentences.

Context:
{context}

Question:
{question}

Answer:
"""

    # Send to Ollama
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    answer = response.json()["response"]

    sources = []

    for meta in retrieved_metadata:
        sources.append(
            f"{meta['filename']} (Page {meta['page']})"
        )

    return answer, sources