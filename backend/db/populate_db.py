from mongodb import inventory

sample_products = [
    {"product_id": "123", "name": "iPhone 15", "category": "smartphones", "stock": 50, "price": 999.99, "description": "Latest Apple iPhone with A16 chip."},
    {"product_id": "124", "name": "Samsung Galaxy S23", "category": "smartphones", "stock": 30, "price": 799.99, "description": "Samsung flagship phone with AMOLED display."},
    {"product_id": "125", "name": "MacBook Pro 14", "category": "laptops", "stock": 20, "price": 1999.99, "description": "Powerful MacBook with M2 chip."}
]

inventory.insert_many(sample_products)
print("Inventory data inserted successfully!")
