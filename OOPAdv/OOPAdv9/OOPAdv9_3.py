# Створити клас, у який дозволяє зберігати дані про студента:
# - ім'я;
# - прізвище;
# - вік;
# - середній бал.
# Створіть список з 10 студентів-інстансів даного класу та протестуйте валідність даних використовуючи пакет unittest.

class Student:
    def __init__(self, firstname: str, lastname: str, age: int, gradepointaverage: float):
        self.__firstname = self.__validate_firstname(firstname)
        self.__lastname = self.__validate_lastname(lastname)
        self.__age = self.__validate_age(age)
        self.__gradepointaverage = self.__validate_gradepointaverage(gradepointaverage)

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        self.__firstname = self.__validate_firstname(value)

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = self.__validate_lastname(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = self.__validate_age(value)

    @property
    def gradepointaverage(self):
        return self.__gradepointaverage

    @gradepointaverage.setter
    def gradepointaverage(self, value):
        self.__gradepointaverage = self.__validate_gradepointaverage(value)

    def __validate_firstname(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        value = value.strip()
        if not value:
            raise ValueError("name cannot be empty")
        return value

    def __validate_lastname(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        value = value.strip()
        if not value:
            raise ValueError("name cannot be empty")
        return value

    def __validate_age(self, value):
        if not isinstance(value, int):
            raise ValueError("quantity must be an integer")
        if value < 0:
            raise ValueError("quantity cannot be negative")
        return value

    def __validate_gradepointaverage(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("quantity must be an integer")
        if value < 0:
            raise ValueError("quantity cannot be negative")
        return value

    def __str__(self):
        return (
            f'Ім\'я: {self.__firstname}, Прізвище: {self.__lastname}, Вік: {self.__age}, Середній бал: {self.__gradepointaverage}'
        )