from pathlib import Path
import json

from AI.AI1.applelaptop import AppleLaptop
from arreyoflaptops import list_laptop

file_path = Path(__file__).parent/"file_for_results.json"

def the_biggest_screen(some_list):
    obj = some_list[0]
    for item in some_list:
        if item.screen_size > obj.screen_size:
            obj = item
    write_to_file(obj)

def the_smallest_screen(some_list):
    obj = some_list[0]
    for item in some_list:
        if item.screen_size < obj.screen_size:
            obj = item
    write_to_file(obj)

def the_most_expensive_laptop(some_list):
    obj = some_list[0]
    for item in some_list:
        if item.price > obj.price:
            obj = item
    write_to_file(obj)

def the_cheapest_laptop(some_list):
    obj = some_list[0]
    for item in some_list:
        if item.price < obj.price:
            obj = item
    write_to_file(obj)

def the_biggest_ram(some_list):
    obj = some_list[0]
    for item in some_list:
        if item.ram > obj.ram:
            obj = item
    write_to_file(obj)

def the_smallest_ram(some_list):
    obj = some_list[0]
    for item in some_list:
        if item.ram < obj.ram:
            obj = item
    write_to_file(obj)

def write_to_file(obj):
    obj_from_file = []
    obj_dict = {"brand": obj.brand, "screen_size": obj.screen_size, "price": obj.price,
        "ram": obj.ram, "model_name": obj.model_name, "processor": obj.processor}

    try:
        if file_path.exists():
            with open(file_path, "r", encoding='utf-8') as f:
                obj_from_file = json.load(f)
        obj_from_file.append(obj_dict)
    except IOError:
        print("Something wrong with reading from file")

    try:
        with open(file_path, "w", encoding='utf-8') as f:
            json.dump(obj_from_file, f, ensure_ascii=False, indent=4)
            #f.write(str(obj) + '\n')

    except IOError:
        print("Something wrong with writing to file")

def read_from_file():
    res_list = []
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            from_file = json.load(f)
        for line in from_file:
            laptop = AppleLaptop(
                line['brand'], line['screen_size'], line['price'],
                line['ram'], line['model_name'], line['processor']
            )
            res_list.append(laptop)
    except IOError:
        print("Something wrong with reading from file")
    iter_obj = iter(res_list)

    while True:
        try:
            item = next(iter_obj)
            print(item)

        except StopIteration:
            break
