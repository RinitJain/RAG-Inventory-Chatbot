from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# Load RAG model
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base")
retriever = RagRetriever.from_pretrained("facebook/rag-token-base", index_name="exact")
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-base", retriever=retriever)

from backend.retriever.retrieval import retrieve_product

def generate_response(user_query):
    product = retrieve_product(user_query)

    # Prepare prompt
    prompt = f"Product: {product['name']}\nDescription: {product['description']}\nStock: {product['stock']}\nPrice: ${product['price']}\n\nUser Query: {user_query}"
    
    input_ids = tokenizer(prompt, return_tensors="pt")["input_ids"]
    generated = model.generate(input_ids)
    response = tokenizer.batch_decode(generated, skip_special_tokens=True)
    
    return response[0]
