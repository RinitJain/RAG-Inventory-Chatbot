# FastAPI for chatbot
from fastapi import FastAPI
from backend.generator.rag_model import generate_response

app = FastAPI()

@app.get("/chat")
def chat(query: str):
    response = generate_response(query)
    return {"response": response}
