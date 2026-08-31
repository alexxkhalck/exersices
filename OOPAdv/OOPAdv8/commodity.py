# Визначити загольну вартість прострочених товарів
# Назва, Ціна, Дата виробництва, Термін придатності, Кількість, Виробник.
# __name, __price, __production_date, __expiration_date, __quantity, __manufacturer.
from datetime import date
from numbers import Real

class Commodity:
    def __init__(self, name: str, price: float, production_date: date, expiration_date: date, quantity: int, manufacturer: str):
        self.__name = self.__validate_name(name)
        self.__price = self.__validate_price(price)
        self.__production_date = self.__validate_production_date(production_date)
        self.__expiration_date = self.__validate_expiration_date(expiration_date)
        self.__quantity = self.__validate_quantity(quantity)
        self.__manufacturer = self.__validate_manufacturer(manufacturer)

    def __validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Назва повинна бути рядком.")
        name = name.strip()
        if not name:
            raise ValueError("Назва не може бути порожньою.")
        return name

    def __validate_price(self, price):
        if not isinstance(price, Real) or isinstance(price, bool):
            raise TypeError("Ціна повинна бути числом.")
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною.")
        return price

    def __validate_production_date(self, value):
        if not isinstance(value, date):
            raise TypeError("Дата виробництва повинна бути об'єктом date.")
        if value > date.today():
            raise ValueError("Дата виробництва не може бути в майбутньому.")
        return value

    def __validate_expiration_date(self, value):
        if not isinstance(value, date):
            raise TypeError("Термін придатності повинен бути об'єктом date.")
        return value

    def __validate_quantity(self, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("Кількість повинна бути цілим числом.")
        if quantity < 0:
            raise ValueError("Кількість не може бути від'ємною.")
        return quantity

    def __validate_manufacturer(self, manufacturer):
        if not isinstance(manufacturer, str):
            raise TypeError("Виробник повинен бути рядком.")
        manufacturer = manufacturer.strip()
        if not manufacturer:
            raise ValueError("Виробник не може бути порожнім.")
        return manufacturer

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = self.__validate_name(name)

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = self.__validate_price(price)

    @property
    def production_date(self):
        return self.__production_date
    @production_date.setter
    def production_date(self, value):
        self.__production_date = self.__validate_production_date(value)

    @property
    def expiration_date(self):
        return self.__expiration_date
    @expiration_date.setter
    def expiration_date(self, value):
        self.__expiration_date = self.__validate_expiration_date(value)

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = self.__validate_quantity(quantity)

    @property
    def manufacturer(self):
        return self.__manufacturer
    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = self.__validate_manufacturer(manufacturer)

    def __str__(self):
        return (
            f"Товар: {self.name}, Ціна: {self.price} грн., Дата виробництва: {self.production_date.strftime('%d.%m.%Y')}\n"
            f"Термін придатності: {self.expiration_date.strftime('%d.%m.%Y')}, Кількість: {self.quantity} шт.\n"
            f"Виробник: {self.manufacturer}")

com1 = Commodity("Молоко", 32.50, date(2026, 8, 1), date(2026, 8, 1), 10, "ТМ «Волошкове поле»")
com2 = Commodity("Хліб", 28.00, date(2026, 8, 29), date(2026, 9, 3), 50, "Київхліб")
com3 = Commodity("Сир", 180.00, date(2026, 8, 15), date(2026, 11, 15), 20, "Молочна країна")
com4 = Commodity("Кава", 250.00, date(2026, 7, 20), date(2027, 7, 20), 15, "Jacobs")
com5 = Commodity("Яблука", 45.00, date(2026, 8, 25), date(2026, 9, 25), 100, "Фермерське господарство «Сад»")
com6 = Commodity("Шоколад", 65.00, date(2026, 8, 10), date(2027, 2, 10), 30, "Конті")

com_list = [com1, com2, com3, com4, com5, com6]