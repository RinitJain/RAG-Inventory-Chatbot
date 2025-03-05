from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from backend.db.mongodb import inventory

# Load embedding model
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Fetch product descriptions
products = list(inventory.find({}, {"_id": 0, "name": 1, "description": 1}))
texts = [p["description"] for p in products]

# Generate embeddings
embeddings = embedder.encode(texts)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Save FAISS index
faiss.write_index(index, "backend/retriever/inventory.index")
print("FAISS index created successfully!")
