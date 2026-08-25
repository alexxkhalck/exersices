# Визначити кількість працівників-інженерів і надрукувати всі відомості про них. Визначити найстаршого та наймолодшого працівника.
# Зробити двома способами: звичайною функцією та лямбдою.
from employees import employees_list

def decorator_count(fn):
    def wrapper(*args):
        func_list = fn(*args)
        counting = 0
        print('Найстарший працівник')
        for item in func_list:
            print(str(item))
            counting += 1
        return counting
    return wrapper

@decorator_count
def count_employees(some_list):
    res_list = []
    for item in some_list:
        if item.position == "Engineer":
            res_list.append(item)
    print('Виконання функції без лямбди')
    return res_list

@decorator_count
def count_employees_lambda(some_list):
    res_list = filter(lambda x: x.position == "Engineer", some_list)
    print('Виконання функції через лямбду')
    return res_list

def the_oldest_employee(some_list):
    mark = some_list[0]
    for item in some_list:
        if item.birthday < mark.birthday:
            mark = item
    return mark

def the_youngest_employee(some_list):
    mark = some_list[0]
    for item in some_list:
        if item.birthday > mark.birthday:
            mark = item
    return mark

def the_oldest_employee_lambda(some_list):
    mark = min(some_list, key=lambda item: item.birthday)
    return mark

def the_youngest_employee_lambda(some_list):
    mark = max(some_list, key=lambda item: item.birthday)
    return mark

result = count_employees(employees_list)
result_lambda = count_employees_lambda(employees_list)
print(f"Кількість інженерів на підприємстві: {result}")
print(f"Кількість інженерів на підприємстві з використанням лямбди: {result_lambda}")
print()
print('Найстарший працівник')
print(the_oldest_employee(employees_list))
print('Найстарший працівник з використанням лямбда')
print(the_oldest_employee_lambda(employees_list))
print()
print('Наймолодший працівник')
print(the_youngest_employee(employees_list))
print('Наймолодший працівник з використанням лямбда')
print(the_youngest_employee_lambda(employees_list))