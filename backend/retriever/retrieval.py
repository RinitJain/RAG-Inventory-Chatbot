import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from backend.db.mongodb import inventory

# Load FAISS index & embedding model
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
index = faiss.read_index("backend/retriever/inventory.index")

# Fetch product details
products = list(inventory.find({}, {"_id": 0, "name": 1, "description": 1, "stock": 1, "price": 1}))

def retrieve_product(query, top_k=1):
    query_embedding = embedder.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    return products[indices[0][0]]  # Return most relevant product
