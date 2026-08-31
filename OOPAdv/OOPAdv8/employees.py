# Визначити кількість співробітників пенсійного віку (чоловікам понад 65, жінкам - 60)
import datetime
from datetime import date

class Employee:
    def __init__(self, last_name: str, first_name: str, middle_name: str, position: str, sex: str, date_of_employment: int):
        self.__last_name = self.__validate_last_name(last_name)
        self.__first_name = self.__validate_first_name(first_name)
        self.__middle_name = self.__validate_middle_name(middle_name)
        self.__position = self.__validate_position(position)
        self.__sex = self.__validate_sex(sex)
        self.__date_of_employment = self.__validate_date_of_employment(date_of_employment)

    def __validate_last_name(self, value):
            if not isinstance(value, str):
                raise ValueError("name must be a string")
            value = value.strip()
            if not value:
                raise ValueError("name cannot be empty")
            return value
    def __validate_first_name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        value = value.strip()
        if not value:
            raise ValueError("name cannot be empty")
        return value
    def __validate_middle_name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        value = value.strip()
        if not value:
            raise ValueError("name cannot be empty")
        return value
    def __validate_position(self, position):
        if not isinstance(position, str):
            raise TypeError("Посада повинна бути рядком.")
        position = position.strip()
        if not position:
            raise ValueError("Посада не може бути порожньою.")
        return position
    def __validate_sex(self, sex):
        if not isinstance(sex, str):
            raise TypeError("Освіта повинна бути рядком.")
        sex = sex.strip()
        if not sex:
            raise ValueError("Освіта не може бути порожньою.")
        return sex
    def __validate_date_of_employment(self, date_of_employment):
        if not isinstance(date_of_employment, datetime.date):
            raise TypeError("Невірна дата народження.")
        if not date_of_employment:
            raise ValueError("Дата народження не може бути порожньою.")
        return date_of_employment

    @property
    def last_name(self):
        return self.__last_name
    @property
    def first_name(self):
        return self.__first_name
    @property
    def middle_name(self):
        return self.__middle_name
    @property
    def position(self):
        return self.__position
    @property
    def sex(self):
        return self.__sex
    @property
    def date_of_employment(self):
        return self.__date_of_employment

    @last_name.setter
    def last_name(self, value):
        self.__last_name = self.__validate_last_name(value)
    @first_name.setter
    def first_name(self, value):
        self.__first_name = self.__validate_first_name(value)
    @middle_name.setter
    def middle_name(self, value):
        self.__middle_name = self.__validate_middle_name(value)
    @position.setter
    def position(self, value):
        self.__position = self.__validate_position(value)
    @sex.setter
    def sex(self, value):
        self.__sex = self.__validate_sex(value)
    @date_of_employment.setter
    def date_of_employment(self, value):
        self.__date_of_employment = self.__validate_date_of_employment(value)

    def __str__(self):
        return (f"Employee(lastname='{self.__last_name}', firstname={self.__first_name}, middlename={self.__middle_name}, "
            f"position='{self.__position}', sex='{self.__sex}', date of employment='{self.__date_of_employment}')")

employee1 = Employee("Шевченко", "Тарас", "Григорович", "fullstack", "male", datetime.date(2000, 3, 9))
employee2 = Employee("Костенко", "Ліна", "Василівна", "frontend", "female", datetime.date(1995, 3, 19))
employee3 = Employee("Франко", "Іван", "Якович", "QA", "male", datetime.date(1990, 8, 27))
employee4 = Employee("Котляревський", "Іван", "Петрович", "backend", "male", datetime.date(1960, 9, 9))
employee5 = Employee("Петрова", "Анна", "Василівна", "frontend", "female", datetime.date(1965, 3, 19))

employees_list = [employee1, employee2, employee3, employee4, employee5]