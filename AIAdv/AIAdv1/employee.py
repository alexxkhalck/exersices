# Прізвище, рік народження, посада, зарплата, освіта

# Визначити кількість працівників інженерів і надрукувати всі відомості про них.

import re

class Employee:
    def __init__(self, lastname, year_of_birth, position, salary, education):
        self.__lastname = self.__validate_lastname(lastname)
        self.__year_of_birth = self.__validate_year_of_birth(year_of_birth)
        self.__position = self.__validate_position(position)
        self.__salary = self.__validate_salary(salary)
        self.__education = self.__validate_education(education)

    def __validate_lastname(self, value):
        if not isinstance(value, str) or not value.isalpha() or len(value) < 2:
            raise ValueError("Не корректне прізвище.")
        return value
    def __validate_year_of_birth(self, value):
        if not isinstance(value, int) or 2026 - value < 16:
            raise ValueError("Вік повинен бути більше 16")
        return value
    def __validate_position(self, value):
        if not isinstance(value, str):
            raise ValueError("Посада не відповідає дійсності.")
        return value
    def __validate_salary(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Не вірний формат.")
        return value
    def __validate_education(self, value):
        if not isinstance(value, str) or len(value) < 2 or not re.fullmatch(r"(Higher|College)", value):
            raise ValueError("Не вірний формат.")

    @property
    def lastname(self):
        return self.__lastname
    @property
    def year_of_birth(self):
        return self.__year_of_birth
    @property
    def position(self):
        return self.__position
    @property
    def salary(self):
        return self.__salary
    @property
    def education(self):
        return self.__education

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname
    @year_of_birth.setter
    def year_of_birth(self, year_of_birth):
        self.__year_of_birth = year_of_birth
    @position.setter
    def position(self, position):
        self.__position = position
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
    @education.setter
    def education(self, education):
        self.__education = education

    def __str__(self):
        return (f"lastname: {self.lastname}, year_of_birthe: {self.year_of_birth}, "
                f"position: {self.position}, salary: {self.salary}, education: {self.education}")

employee1 = Employee("Ivanov", 1985, "Manager", 30000, "Higher")
employee2 = Employee("Petrov", 1990, "Engineer", 35000, "Higher")
employee3 = Employee("Sidorov", 1988, "Accountant", 28000, "Higher")
employee4 = Employee("Brown", 1995, "Engineer", 40000, "Higher")
employee5 = Employee("Smith", 1982, "Director", 60000, "Higher")

employees = [employee1, employee2, employee3, employee4, employee5]

for i in filter(lambda x: x.position == 'Engineer', employees):
    print(i)

res_list = list(filter(lambda x: x.position == 'Engineer', employees))
for i in res_list:
    print(i)