# Визначити найдорожчій товар на складі та надрукувати всі відомості про нього. Найдешевший товар на складі. Вивести результати в
# файл JSON та надрукувати в консо
import json
from pathlib import Path
from products import products_list

json_file = Path(__file__).parent/"products_file.json"

def save_to_json(fn):
    def wrapper(*args):
        res = fn(*args)
        data_for_saving = [
            {
                "name": res.name,
                "quantity": res.quantity,
                "price": res.price,
                "year_of_manufacture": res.year_of_manufacture,
                "manufacturer": res.manufacturer
            }
        ]
        try:
            with open(json_file, "a", encoding="utf-8") as f:
                json.dump(data_for_saving, f, ensure_ascii=False, indent=4)
        except IOError:
            print('1111111111111111111')
        return res
    return wrapper

@save_to_json
def the_most_expensive(some_list):
    print('Найдорожчий товар.')
    res = max(some_list, key=lambda x: x.price)
    return res

@save_to_json
def the_cheepest(some_list):
    print('Найдешевший товар.')
    res = min(some_list, key=lambda y: y.price)
    return res

print(str(the_most_expensive(products_list)))
print(str(the_cheepest(products_list)))