# Створіть список товарів в інтернет-магазині. Серіалізуйте його за допомогою pickle та збережіть у JSON.
import pickle
import json
import base64

products = [
    {"name": "Laptop", "price": 30000, "quantity": 10},
    {"name": "Mouse", "price": 500, "quantity": 50},
    {"name": "Keyboard", "price": 1500, "quantity": 30},
    {"name": "Monitor", "price": 7000, "quantity": 15},
    {"name": "Headphones", "price": 1200, "quantity": 20},
]

pickled_data = pickle.dumps(products)

pickled_b64 = base64.b64encode(pickled_data).decode("utf-8")

data_for_json = {
    "pickled_products": pickled_b64
}

with open("products_pickled.json", "w", encoding="utf-8") as f:
    json.dump(data_for_json, f, ensure_ascii=False, indent=4)

with open("products_pickled.json", "r", encoding="utf-8") as f:
    loaded_json = json.load(f)

pickled_b64_loaded = loaded_json["pickled_products"]
pickled_bytes = base64.b64decode(pickled_b64_loaded)
restored_products = pickle.loads(pickled_bytes)

print(restored_products)