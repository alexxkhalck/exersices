from arrayofobj import products
from arreyofprod import shopprod
from pathlib import Path

file_path = Path(__file__).parent/'prod_file.txt'

# методи до третьої задачі
def searching_prod(products):
    quantity = 0
    obj = None
    for item in products:
        if item.quantity > quantity:
            quantity = item.quantity
            obj = item
    print(obj.__str__())
    write_in_file(obj)

def write_in_file(input_obj):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(input_obj.quantity) + '\n' + str(input_obj.price) + '\n' + str(input_obj.year_of_manufacture) + '\n' + input_obj.manufacturer)
    except IOError:
        print('Помилка запису.')

def read_from_file():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            print(f.read())
    except IOError:
        print('Помилка читання.')

# методи до першої задачі
def amount_of_ram(shopprod):
    res_list = []
    for item in shopprod:
        if item.amount_of_RAM > 10:
            res_list.append(item)
    write_in_file_prod(res_list)

def write_in_file_prod(some_list):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for item in some_list:
                f.write(f'1: {item.name}, 2: {item.frequency}, 3: {item.amount_of_RAM}, 4: {item.presence_of_DVD_ROM}, 5: {item.cost} \n')
    except IOError:
        print('Помилка запису.')

def read_from_file_prod():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                print(line)
    except IOError:
        print('Помилка читання.')