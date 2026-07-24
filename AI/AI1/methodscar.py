from arreyofcars import list_cars
from pathlib import Path

file_path = Path(__file__).parent/'writing_to_file.txt'

def run_tasks():
    the_newest_car(list_cars)
    the_oldest_car(list_cars)
    the_cheepest_car(list_cars)
    the_expensive_car(list_cars)
    the_most_powerful(list_cars)
    the_less_powerful(list_cars)

def the_newest_car(some_list):
    res_list = []
    temp = some_list[0]
    for item in some_list:
        if item.year > temp.year:
            temp = item
    for item in some_list:
        if temp.year == item.year:
            res_list.append(item)
    write_to_cars_file(res_list)

def the_oldest_car(some_list):
    res_list = []
    temp = some_list[0]
    for item in some_list:
        if temp.year > item.year:
            temp = item
    for item in some_list:
        if temp.year == item.year:
            res_list.append(temp)
    write_to_cars_file(res_list)

def the_cheepest_car(some_list):
    res_list = []
    temp = some_list[0]
    for item in some_list:
        if item.price < temp.price:
            temp = item
    for item in some_list:
        if temp.price == item.price:
            res_list.append(temp)
    write_to_cars_file(res_list)

def the_expensive_car(some_list):
    res_list = []
    temp = some_list[0]
    for item in some_list:
        if item.price > temp.price:
            temp = item
    for item in some_list:
        if temp.price == item.price:
            res_list.append(temp)
    write_to_cars_file(res_list)

def the_most_powerful(some_list):
    res_list = []
    temp = some_list[0]
    for item in some_list:
        if item.horsepower > temp.horsepower:
            temp = item
    for item in some_list:
        if temp.horsepower == item.horsepower:
            res_list.append(temp)
    write_to_cars_file(res_list)

def the_less_powerful(some_list):
    res_list = []
    temp = some_list[0]
    for item in some_list:
        if item.horsepower < temp.horsepower:
            temp = item
    for item in some_list:
        if temp.horsepower == item.horsepower:
            res_list.append(temp)
    write_to_cars_file(res_list)

def write_to_cars_file(some_list):
    try:
        with open(file_path,'a',encoding='utf-8') as f:
            for item in some_list:
                f.write(str(item)+'\n')
    except IOError:
        print('Error with writing to file.')

def read_from_cars_file():
    res_list = []
    try:
        with open(file_path,'r',encoding='utf-8') as f:
            for item in f:
                res_list.append(item.strip())
    except FileNotFoundError:
        print('Error with reading from file.')

    iter_obj = iter(res_list)

    while True:
        try:
            item = next(iter_obj)
            print(item)
        except StopIteration:
            break