# Створіть модуль для отримання простих чисел. Імпортуйте його з іншого модуля. Імпортуйте його окремі імена.
def is_prime(num):
    if num < 2:
        return False
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            return False
    return True

def simple_numbers(input_number):
    res_list = []
    for i in range(2, input_number + 1):
        if is_prime(i):
            res_list.append(i)
    return res_list

def write_in_file(list_num, path_list):
    try:
        with open(path_list, 'w', encoding='utf-8') as f:
            for i in list_num:
                f.write(str(i) + '\n')
    except IOError:
        print('Якась помилка запису!!!')

def read_from_file(path_list):
    try:
        with open(path_list, 'r', encoding='utf-8') as f:
            for line in f:
                print(line)
    except IOError:
        print('Якась помилка читання!!!')