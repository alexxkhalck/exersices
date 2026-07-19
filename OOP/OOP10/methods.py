from pathlib import Path

file_path = Path(__file__).parent/"file.txt"
the_expensive_path = Path(__file__).parent/"the_expensive.txt"

def writing_to_file(some_list):
    try:
        with open(file_path, "w", encoding="utf_8") as f:
            for item in some_list:
                user_year = item.year_of_birth
                age = 2026 - user_year
                if age >= 60:
                    f.write(str(item) + "\n")
    except IOError:
        print('Помилка запису.')

def read_from_file():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            print(f.read())
    except IOError:
        print('Помилка читання.')

def writing_to_file_ex(some_list):
    try:
        with open(the_expensive_path, "w", encoding="utf_8") as f:
            temp = some_list[0]
            for item in some_list:
                if item.price > temp.price:
                    temp = item
            f.write(f"Name: {temp.name}, Quantity: {temp.quantity}, Price: {temp.price}, Year of manufacture: {temp.year_of_manufacture}, Manufacturer: {temp.manufacturer}")
    except IOError:
        print('Помилка запису.')

def read_from_file_ex():
    try:
        with open(the_expensive_path, 'r', encoding='utf-8') as f:
            print(f.read())
    except IOError:
        print('Помилка читання.')