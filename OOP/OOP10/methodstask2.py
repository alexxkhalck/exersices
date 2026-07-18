import re
from pathlib import Path

user_file = Path(__file__).parent/'datas.txt'

def writing_to_file(some_list):
    try:
        with open(user_file, 'w', encoding='utf-8') as f:
            for item in some_list:
                f.write(f'{str(item)}')
    except IOError:
        print('Помилка запису в файл.')

def read_from_file():
    res = ''
    try:
        with open(user_file, 'r', encoding='utf-8') as f:
            res = f.readlines()
    except IOError:
        print('Помилка запису в файл.')
    return res

def get_data(obj):
    for item in obj:
        birthday = re.findall(r'\d{2}\.\d{2}\.\d{4}', item)
        phone_num = re.findall(r'\+380\d{9}', item)
        email = re.findall(r'[\w._%+-]+@\w+\.\w+', item)
        data_list = [birthday,phone_num,email]
        writing_to_another_file(data_list)

def writing_to_another_file(some_list):
    u_file = Path(__file__).parent/'datarewrite.txt'
    try:
        with open(u_file, 'a', encoding='utf-8') as f:
            f.write(f'{str(some_list)}')

    except IOError:
        print('Помилка запису в rewriteddata файл.')