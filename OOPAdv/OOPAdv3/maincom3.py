from  commodity3 import commodity_list
from  commodity3 import UserCommodity
from pathlib import Path
import json

path_json_file = Path(__file__).parent / 'commodity.json'

def commodity_decorator(fn):
    def wrapper(*args, **kwargs):
        result = list(filter(lambda x: x.price == fn(commodity_list), commodity_list))
        return result
    return wrapper

@commodity_decorator
def the_most_expensive_commodity(some_list):
    y = max(x.price for x in some_list)
    return y

expensive_commodity = the_most_expensive_commodity(commodity_list)
print('FIRST')
for item in expensive_commodity:
    print(item)

def save_to_file(obj):
    data_to_file = [
        {
            "name": item.name,
            "quantity": item.quantity,
            "price": item.price,
            "manufacturer": item.manufacturer,
            "date_of_arrival_in_warehouse": item.date_of_arrival_in_warehouse
        }
        for item in obj
    ]
    try:
        with open(path_json_file, 'w', encoding='utf-8') as f:
            json.dump(data_to_file, f, ensure_ascii=False, indent=4)
    except IOError:
        print('1111111111111111111')

def load_from_file():
    try:
        with open(path_json_file, 'r', encoding='utf-8') as f:
            obj = json.load(f)
            res_obj = [
                UserCommodity(
                    name=item['name'],
                    quantity=item['quantity'],
                    price=item['price'],
                    manufacturer=item['manufacturer'],
                    date_of_arrival_in_warehouse=item['date_of_arrival_in_warehouse']
                )
                for item in obj
            ]
            return res_obj
    except FileNotFoundError:
        print("Файл не знайдено")
        return []
    except json.JSONDecodeError:
        print("У файлі некоректний JSON")
        return []

print('SECOND')
for item in the_most_expensive_commodity(commodity_list):
    print(item)

save_to_file(expensive_commodity)
obj_from_file = iter(load_from_file())
for item in obj_from_file:
    print(str(item))