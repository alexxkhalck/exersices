# Марка авто, виробник, тип, рік випуску, дата проходження техогляду, дата реєстрації
# Вивести відомості про авто, які пройшли техогляд менше ніж один рік
from datetime import date


class Car:
    def __init__(self, car_brand: str, manufacturer: str, type: str, year_of_manufacture: int, inspection_date: date,
                 registration_date: date):
        self.__car_brand = self.__validate_car_brand(car_brand)
        self.__manufacturer = self.__validate_manufacturer(manufacturer)
        self.__type = self.__validate_type(type)
        self.__year_of_manufacture = self.__validate_year_of_manufacture(year_of_manufacture)
        self.__inspection_date = self.__validate_inspection_date(inspection_date)
        self.__registration_date = self.__validate_registration_date(registration_date)

    def __validate_car_brand(self, value):
        if not isinstance(value, str):
            raise TypeError("Марка авто повинна бути рядком.")
        value = value.strip()
        if not value:
            raise ValueError("Марка авто не може бути порожньою.")
        return value

    def __validate_manufacturer(self, value):
        if not isinstance(value, str):
            raise TypeError("Виробник повинен бути рядком.")
        value = value.strip()
        if not value:
            raise ValueError("Виробник не може бути порожнім.")
        return value

    def __validate_type(self, value):
        if not isinstance(value, str):
            raise TypeError("Тип авто повинен бути рядком.")
        value = value.strip()
        if not value:
            raise ValueError("Тип авто не може бути порожнім.")
        return value

    def __validate_year_of_manufacture(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("Рік випуску повинен бути цілим числом.")
        current_year = date.today().year
        if value < 1886 or value > current_year:
            raise ValueError(
                f"Рік випуску повинен бути від 1886 до {current_year}."
            )
        return value

    def __validate_inspection_date(self, value):
        if not isinstance(value, date):
            raise TypeError("Дата техогляду повинна бути об'єктом date.")
        return value

    def __validate_registration_date(self, value):
        if not isinstance(value, date):
            raise TypeError("Дата реєстрації повинна бути об'єктом date.")
        return value

    @property
    def car_brand(self):
        return self.__car_brand
    @car_brand.setter
    def car_brand(self, value):
        self.__car_brand = self.__validate_car_brand(value)

    @property
    def manufacturer(self):
        return self.__manufacturer
    @manufacturer.setter
    def manufacturer(self, value):
        self.__manufacturer = self.__validate_manufacturer(value)

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, value):
        self.__type = self.__validate_type(value)

    @property
    def year_of_manufacture(self):
        return self.__year_of_manufacture
    @year_of_manufacture.setter
    def year_of_manufacture(self, value):
        self.__year_of_manufacture = self.__validate_year_of_manufacture(value)

    @property
    def inspection_date(self):
        return self.__inspection_date
    @inspection_date.setter
    def inspection_date(self, value):
        self.__inspection_date = self.__validate_inspection_date(value)

    @property
    def registration_date(self):
        return self.__registration_date
    @registration_date.setter
    def registration_date(self, value):
        self.__registration_date = self.__validate_registration_date(value)

    def __str__(self):
        return (
            f"Автомобіль: {self.car_brand}, Виробник: {self.manufacturer}, Тип: {self.type}, Рік випуску: {self.year_of_manufacture}, "
            f"Дата техогляду: {self.inspection_date.strftime('%d.%m.%Y')}, Дата реєстрації: {self.registration_date.strftime('%d.%m.%Y')}"
        )

car1 = Car("Toyota Camry", "Toyota Motor Corporation", "Седан", 2021, date(2025, 5, 10), date(2025, 3, 15))
car2 = Car("Cadillac Escalade", "General Motors Company", "Універсал", 2022, date(2026, 5, 10), date(2023, 3, 15))
car3 = Car("Volkswagen transporter", "Volkswagen", "Мікроавтобус", 2023, date(2026, 2, 10), date(2024, 3, 15))
car4 = Car("Nissan Qashqai", "Nissan Motor Co., Ltd.", "Седан", 2011, date(2025, 12, 10), date(2026, 3, 15))
car5 = Car("Renault Duster", "Renault Group", "Кросовер", 2017, date(2026, 5, 19), date(2025, 3, 15))

cars_list = [car1, car2, car3, car4, car5]