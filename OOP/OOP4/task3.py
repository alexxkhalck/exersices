# Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи.
# Конструктор має генерувати виняток, якщо вказано неправильні дані. Введіть список працівників із
# клавіатури. Виведіть усіх співробітників, які були прийняті після цього року.
from datetime import date


class Employee:
    def __init__(self, name, lastname, department, year_of_start_of_work):
        if not isinstance(name, str):
            raise ValueError("Не корректне ім'я.")
        if not isinstance(lastname, str):
            raise ValueError("Не корректне прізвище.")
        if not isinstance(department, str):
            raise ValueError("Не корректний відділ.")
        if year_of_start_of_work > date.today().year:
            raise ValueError("Ви ввели не вірний рік.")

        self.__name = name
        self.__lastname = lastname
        self.__department = department
        self.__year_of_start_of_work = year_of_start_of_work

    @property
    def name(self):
        return self.__name

    @property
    def lastname(self):
        return self.__lastname

    @property
    def department(self):
        return self.__department

    @property
    def year_of_start_of_work(self):
        return self.__year_of_start_of_work

    @name.setter
    def name(self, name):
        self.__name = name

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @department.setter
    def department(self, department):
        self.__department = department

    @year_of_start_of_work.setter
    def year_of_start_of_work(self, year_of_start_of_work):
        self.__year_of_start_of_work = year_of_start_of_work


def some_print(res):
    for e in res:
        print(f'name: {e.name}, lastname: {e.lastname}, department: {e.department}, year: {e.year_of_start_of_work}')


def comparing(ist_of_employees, flag_year):
    # Список для фільтру співробітників за роком
    res = []
    for e in list_of_employees:
        if e.year_of_start_of_work > flag_year:
            res.append(e)
    return res


emp1 = Employee('Степан', 'Степанов', 'Продаж', 2024)
emp2 = Employee('Іван', 'Іванов', 'Реклама', 2012)
emp3 = Employee('Петро', 'Петров', 'Закупівлі', 2025)
emp4 = Employee('Олексій', 'Олексієв', 'Продажів', 2013)

# Список співробітників
list_of_employees = [emp1, emp2, emp3, emp4]

flag_year = int(input('Введіть рік для фільтру.'))

filtered_list = comparing(list_of_employees, flag_year)

some_print(filtered_list)