from pathlib import Path
from arreyoflaptops import list_laptop

file_path = Path(__file__).parent/"file_for_results.txt"

def the_biggest_screen(some_list):
    obj = some_list[0]
    for item in some_list:
        if item.screen_size > obj.screen_size:
            obj = item
    write_to_file(obj)

def the_smollest_screen(some_list):
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

def the_beggest_ram(some_list):
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
    try:
        with open(file_path, "a", encoding='utf-8') as f:
            f.write(str(obj) + '\n')

    except IOError:
        print("Something wrong with writing to file")

def read_from_file():
    res_list = []
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            for line in f:
                res_list.append(line)
    except IOError:
        print("Something wrong with reading from file")
    iter_obj = iter(res_list)

    while True:
        try:
            item = next(iter_obj)
            print(item)

            # print(f"Brand: {item.brand}, Screensize: {item.screen_size} Price: {item.price}, "
            #       f"RAM: {item.ram}, Model: {item.model}, Processor: {item.processor}")
        except StopIteration:
            break
