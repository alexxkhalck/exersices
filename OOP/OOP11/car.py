# марка авто виробник тип рік випуску дата реєстрації
# Вивести відомості про машини марки Тойота, зареєстровані до 2007-го року
# car brand manufacturer type year of manufacture registration date
class Car:
    def __init__(self, car_brand, manufacturer, type, year_of_manufacture, registration_date):
        self.__car_brand = self.__validate_car_brand(car_brand)
        self.__manufacturer = self.__validate_manufacturer(manufacturer)
        self.__type = self.__validate_type(type)
        self.__year_of_manufacture = self.__validate_year_of_manufacture(year_of_manufacture)
        self.__registration_date = self.__validate_registration_date(registration_date)

    @property
    def car_brand(self):
        return self.__car_brand

    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def type(self):
        return self.__type

    @property
    def year_of_manufacture(self):
        return self.__year_of_manufacture

    @property
    def registration_date(self):
        return self.__registration_date

    @car_brand.setter
    def car_brand(self, value):
        self.__car_brand = self.__validate_car_brand(value)

    @manufacturer.setter
    def manufacturer(self, value):
        self.__manufacturer = self.__validate_manufacturer(value)

    @type.setter
    def type(self, value):
        self.__type = self.__validate_type(value)

    @year_of_manufacture.setter
    def year_of_manufacture(self, value):
        self.__year_of_manufacture = self.__validate_year_of_manufacture(value)

    @registration_date.setter
    def registration_date(self, value):
        self.__registration_date = self.__validate_registration_date(value)

    def __validate_car_brand(self, value):
        if not isinstance(value, str):
            raise ValueError("car_brand must be a string")
        value = value.strip()
        if not value:
            raise ValueError("car_brand cannot be empty")
        return value

    def __validate_manufacturer(self, value):
        if not isinstance(value, str):
            raise ValueError("manufacturer must be a string")
        value = value.strip()
        if not value:
            raise ValueError("manufacturer cannot be empty")
        return value

    def __validate_type(self, value):
        if not isinstance(value, str):
            raise ValueError("type must be a string")
        value = value.strip()
        if not value:
            raise ValueError("type cannot be empty")
        return value

    def __validate_year_of_manufacture(self, value):
        if not isinstance(value, int):
            raise ValueError("year_of_manufacture must be an integer")
        if value < 1886 or value > 2026:
            raise ValueError("year_of_manufacture is invalid")
        return value

    def __validate_registration_date(self, value):
        if not isinstance(value, str):
            raise ValueError("registration_date must be a string in format DD.MM.YYYY")
        value = value.strip()
        if not value:
            raise ValueError("registration_date cannot be empty")
        return value

    def __str__(self):
        return (
            f"Car(car_brand={self.car_brand}, manufacturer={self.manufacturer}, "
            f"type={self.type}, year_of_manufacture={self.year_of_manufacture}, "
            f"registration_date={self.registration_date})"
        )