from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb://localhost:27017/")
    return client["ecommerce_db"]

db = get_database()
inventory = db["products"]
