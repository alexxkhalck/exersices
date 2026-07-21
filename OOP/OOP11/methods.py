from pathlib import Path
import re

path_to_file_emps = Path(__file__).parent/"path_to_file_emps.txt"
path_to_file_car = Path(__file__).parent/"path_to_file_car.txt"

def mid_arithmetic(some_list):
    res_list = []
    result = sum(item.salary for item in some_list)/len(some_list)
    for item in some_list:
        user_year = re.fullmatch(r"\d{2}\.\d{2}\.(\d{4})", item.date_of_birth)
        age = 2026 - int(user_year.group(1))
        if item.salary > result and age < 30:
            res_list.append(item)
    write_to_file_emps(res_list)

def write_to_file_emps(some_list):
    try:
        with open(path_to_file_emps, "w", encoding="utf-8") as f:
            for item in some_list:
                f.write(str(item))
    except IOError:
        print('Помилка запису в файл 1.')

def read_to_file_emps():
    try:
        with open(path_to_file_emps, "r", encoding="utf-8") as f:
            print(f.readlines())
    except IOError:
        print('Помилка зчитування з файл 1.')

def registration(some_list):
    res_list = []
    for item in some_list:
        reg_date = re.fullmatch(r'\d{2}\.\d{2}\.(\d{4})', item.registration_date)
        #reg_year = int(reg_date.group(1))
        if item.car_brand == "Toyota" and int(reg_date.group(1)) < 2007:
            res_list.append(item)
    # for item in res_list:
    #     print(item.__str__())
    write_to_file_car(res_list)

def write_to_file_car(some_list):
    try:
        with open(path_to_file_car, "w", encoding="utf-8") as f:
            for item in some_list:
                f.write(str(item))
    except IOError:
        print('Помилка запису в файл 2.')

def read_to_file_car():
    try:
        with open(path_to_file_car, "r", encoding="utf-8") as f:
            print(f.readlines())
    except IOError:
        print('Помилка зчитування з файл 2.')