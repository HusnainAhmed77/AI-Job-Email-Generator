import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction



embedding_func = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

client = chromadb.Client()
collection = client.get_or_create_collection(name="resume_data", embedding_function=embedding_func)

def save_resume(user_id: str, resume_text: str):
    collection.add(
        documents=[resume_text],
        ids=[user_id]
    )

def get_resume(user_id: str) -> str:
    result = collection.get(ids=[user_id])
    return result["documents"][0] if result["documents"] else ""