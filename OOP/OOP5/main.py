# Легка задача))
# Прізвище
# Вік
# Кількість ігор
# Кількість пропущених шайб
#
# Визначити середній вік хокеїстів і вивести відомості про хокеїстів, вік яких понад 25 років.
# class Hockey:
#     def __init__(self, lastname, age, number_of_games, number_of_goals_conceded):
#         self.__lastname = lastname
#         self.__age = age
#         self.__number_of_games = number_of_games
#         self.__number_of_goals_conceded = number_of_goals_conceded
#
#     @property
#     def lastname(self):
#         return self.__lastname
#     @property
#     def age(self):
#         return self.__age
#     @property
#     def number_of_games(self):
#         return self.__number_of_games
#     @property
#     def number_of_goals_conceded(self):
#         return self.__number_of_goals_conceded
#
#     @lastname.setter
#     def lastname(self, lastname):
#         self.__lastname = lastname
#     @age.setter
#     def age(self, age):
#         self.__age = age
#     @number_of_games.setter
#     def number_of_games(self, number_of_games):
#         self.__number_of_games = number_of_games
#     @number_of_goals_conceded.setter
#     def number_of_goals_conceded(self, number_of_goals_conceded):
#         self.__number_of_goals_conceded = number_of_goals_conceded
#
# def average_age(some_list):
#     average_ages = 0
#     for hok in some_list:
#         average_ages += hok.age
#     average_ages = average_ages / len(some_list)
#     return average_ages
#
# def info_about_age_bigger_then(some_list, flag_age):
#     result = []
#     for hok in some_list:
#         if hok.age > flag_age:
#             result.append(hok)
#     return result
#
# hok1 = Hockey("Hokkid", 22, 10, 5)
# hok2 = Hockey("Gokkid", 26, 11, 3)
# hok3 = Hockey("Tokkid", 23, 12, 6)
# hok4 = Hockey("Mokkid", 27, 15, 7)
# hok5 = Hockey("Dokkid", 24, 11, 4)
# hok6 = Hockey("Pokkid", 26, 12, 5)
#
# list_of_hoks = [hok1, hok2, hok3, hok4, hok5, hok6]
# average_age = average_age(list_of_hoks)
# print('Середній вік хокеїстів: ', average_age)
# age_bigger_then = info_about_age_bigger_then(list_of_hoks, 25)
# for item in age_bigger_then:
#     print(f'{item.lastname}, Вік: {item.age}, зіграно: {item.number_of_games}, голів забито: {item.number_of_goals_conceded}')
class Employee:
    def __init__(self, name, salary, years):
        if not isinstance(name, str):
            raise ValueError('Name must be a string and cannot be of empty')
        if not isinstance(salary, int):
            raise ValueError('Name must be an integer and cannot be of empty')
        if not isinstance(years, int):
            raise ValueError('Name must be an integer and cannot be of empty')

        self.__name = name
        self.__salary = salary
        self.__years = years

    @property
    def name(self):
        return self.__name
    @property
    def salary(self):
        return self.__salary
    @property
    def years(self):
        return self.__years

    @name.setter
    def name(self, name):
        self.__name = name
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
    @years.setter
    def years(self, years):
        self.__years = years

    def __str__(self):
        print(f'Name: {self.name}, Salary: {self.salary}, Years: {self.years}')

    @staticmethod
    def increase_salary(list_of_emp):
        for emp in list_of_emp:
            if emp.years >= 10:
                emp.salary = emp.salary * 1.20
            elif 5 <= emp.years < 10:
                emp.salary = emp.salary * 1.10
            elif emp.years < 5:
                emp.salary = emp.salary * 1.05
        return list_of_emp

class Manager(Employee):
    def __init__(self, name, salary, years, department):
        super().__init__(name, salary, years)
        if not isinstance(name, str):
            raise ValueError('Name must be a string and cannot be of empty')
        if not isinstance(salary, int):
            raise ValueError('Salary must be an integer and cannot be of empty')
        if not isinstance(years, int):
            raise ValueError('Years must be an integer and cannot be of empty')
        if not isinstance(department, str):
            raise ValueError('Department must be a string and cannot be of empty')
        self.__name = name
        self.__salary = salary
        self.__years = years
        self.__department = department

    @property
    def name(self):
        return self.__name
    @property
    def salary(self):
        return self.__salary
    @property
    def years(self):
        return self.__years
    @property
    def department(self):
        return self.__department


    @name.setter
    def name(self, name):
        self.__name = name
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
    @years.setter
    def years(self, years):
        self.__years = years
    @department.setter
    def department(self, department):
        self.__department = department

    def __str__(self):
        print(f'Name: {self.name}, Salary: {self.salary}, Years: {self.years}, Department: {self.department}')

def selection_by_term_more_then_10(list_of_emp):
    first_list = []
    for employee in list_of_emp:
        if employee.years >= 10:
            first_list.append(employee)
    return first_list

def selection_by_term_more_then_5(list_of_emp):
    second_list = []
    for employee in list_of_emp:
        if 5 <= employee.years < 10:
            second_list.append(employee)
    return second_list

def selection_by_term_lass_then_5(list_of_emp):
    third_list = []
    for employee in list_of_emp:
        if employee.years < 5:
            third_list.append(employee)
    return third_list

em1 = Employee("Sam", 15000, 5)
em2 = Employee("Jack", 15000, 3)
em3 = Manager("Jim", 25000, 13, 'manager')
em4 = Employee("Helen", 20000, 12)
em5 = Employee("Derek", 10000, 7)
em6 = Manager("Will", 15000, 2, 'manager')

list_of_employees = [em1, em2, em3, em4, em5, em6]
for employee in list_of_employees:
    if type(employee) is Employee:
        print(f'Name: {employee.name}, Salary: {employee.salary}, Years: {employee.years}')
    elif type(employee) is Manager:
        print(f'Name: {employee.name}, Salary: {employee.salary}, Years: {employee.years}, Department{employee.department}')

print('Через __str__')
for employee in list_of_employees:
    print(employee)

list_more_then_10 = selection_by_term_more_then_10(list_of_employees)
list_more_then_5 = selection_by_term_more_then_5(list_of_employees)
list_less_then_5 = selection_by_term_lass_then_5(list_of_employees)

print()
print()

list_more_then_10 = Employee.increase_salary(list_more_then_10)
list_more_then_5 = Employee.increase_salary(list_more_then_5)
list_less_then_5 = Employee.increase_salary(list_less_then_5)
for employee in list_more_then_10:
    if type(employee) is Employee:
        print(f'Name: {employee.name}, Salary: {employee.salary}, Years: {employee.years}')
    elif type(employee) is Manager:
        print(f'Name: {employee.name}, Salary: {employee.salary}, Years: {employee.years}, Department{employee.department}')

for employee in list_more_then_5:
    if type(employee) is Employee:
        print(f'Name: {employee.name}, Salary: {employee.salary}, Years: {employee.years}')
    elif type(employee) is Manager:
        print(f'Name: {employee.name}, Salary: {employee.salary}, Years: {employee.years}, Department{employee.department}')

for employee in list_less_then_5:
    if type(employee) is Employee:
        print(f'Name: {employee.name}, Salary: {employee.salary}, Years: {employee.years}')
    elif type(employee) is Manager:
        print(f'Name: {employee.name}, Salary: {employee.salary}, Years: {employee.years}, Department{employee.department}')
