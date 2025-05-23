# RAG-Inventory-Chatbot

## Setup Instructions

This application requires a running MongoDB instance.

**MongoDB Configuration:**
- The application attempts to connect to MongoDB using the following URI: `mongodb://localhost:27017/`.
- The database named `ecommerce_db` and the collection `products` will be used (and created if they don't exist).
- Ensure your MongoDB server is running and accessible at this URI.
- If your MongoDB is configured differently (e.g., different host, port, or requires authentication), you will need to modify the connection string in `backend/db/mongodb.py` accordingly.

```python
# backend/db/mongodb.py
from pymongo import MongoClient

def get_database():
    # Update this line if your MongoDB setup is different
    client = MongoClient("mongodb://localhost:27017/") 
    return client["ecommerce_db"]

db = get_database()
inventory = db["products"]
```

### Data Population and Indexing

Before running the main application, you need to populate the database and generate the FAISS index for semantic search.

**1. Populate the Database:**
   - Open your terminal and navigate to the root directory of this project.
   - Ensure your `PYTHONPATH` includes the `backend` directory or run the script as a module. A simple way to handle imports correctly is to run the script from the project's root directory as a module:
     ```bash
     python -m backend.db.populate_db
     ```
   - This script will insert sample product data into the `products` collection in your `ecommerce_db` MongoDB database.
   - You should see a confirmation message: "Inventory data inserted successfully!"

**2. Generate FAISS Index:**
   - After populating the database, you need to generate embeddings for the product descriptions and create a FAISS index.
   - From the project's root directory, run the following command:
     ```bash
     python -m backend.retriever.embeddings
     ```
   - This script will:
     - Fetch product descriptions from MongoDB.
     - Generate sentence embeddings for these descriptions.
     - Create a FAISS index and save it to `backend/retriever/inventory.index`.
   - You should see a confirmation message: "FAISS index created successfully!"

**Important:**
- Ensure MongoDB is running and accessible *before* running these scripts.
- The `embeddings.py` script depends on the data populated by `populate_db.py`. Run them in the order specified.

## Running the Chatbot

Once you have set up MongoDB, populated the database, and generated the FAISS index, you can run the chatbot application.

**1. Install Dependencies:**
   - Navigate to the project's root directory in your terminal.
   - It is highly recommended to use a Python virtual environment.
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install the required Python packages from the `backend` directory:
     ```bash
     pip install -r backend/requirements.txt
     ```

**2. Run the Application:**
   - Ensure you are in the project's root directory.
   - Run the FastAPI application using Uvicorn:
     ```bash
     python -m backend.main
     ```
   - This will start the server, typically on `http://0.0.0.0:8000`.
   - You should see output from Uvicorn indicating the server is running.

**3. Interact with the Chatbot:**
   - The chatbot exposes a GET endpoint at `/chat`.
   - You can interact with it using your browser or a tool like `curl`.
   - Open your browser and go to `http://localhost:8000/chat?query=your%20question%20here`.
   - Or, using `curl` from your terminal:
     ```bash
     curl "http://localhost:8000/chat?query=Tell%20me%20about%20iPhones"
     ```
   - The response will be a JSON object containing the chatbot's answer. For example:
     ```json
     {
         "response": "The iPhone 15 is the latest Apple iPhone with A16 chip."
     }
     ```
