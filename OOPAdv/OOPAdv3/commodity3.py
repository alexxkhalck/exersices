# Назва, кількість, ціна, рік виготовлення, виробник
# Визначити найдорожчий товар на складі та надрукувати всі відомості про нього
class UserCommodity:
    def __init__(self, name, quantity, price, manufacturer, date_of_arrival_in_warehouse):
        self.__name = self.__validate_name(name)
        self.__quantity = self.__validate_quantity(quantity)
        self.__price = self.__validate_price(price)
        self.__manufacturer = self.__validate_manufacturer(manufacturer)
        self.__date_of_arrival_in_warehouse = self.__validate_date_of_arrival_in_warehouse(date_of_arrival_in_warehouse)

    @property
    def name(self):
        return self.__name
    @property
    def quantity(self):
        return self.__quantity
    @property
    def price(self):
        return self.__price
    @property
    def manufacturer(self):
        return self.__manufacturer
    @property
    def date_of_arrival_in_warehouse(self):
        return self.__date_of_arrival_in_warehouse

    @name.setter
    def name(self, name):
        self.__name = name
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
    @price.setter
    def price(self, price):
        self.__price = price
    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer
    @date_of_arrival_in_warehouse.setter
    def date_of_arrival_in_warehouse(self, date_of_arrival_in_warehouse):
        self.__date_of_arrival_in_warehouse = date_of_arrival_in_warehouse

    def __validate_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        if not value:
            raise ValueError('Name cannot be empty')
        return value
    def __validate_quantity(self, value):
        if not isinstance(value, int):
            raise TypeError('Quantity must be a integer')
        if not value:
            raise ValueError('Quantity cannot be empty')
        return value
    def __validate_price(self, value):
        if not isinstance(value, int):
            raise TypeError('Price must be a integer')
        if not value:
            raise ValueError('Price cannot be empty')
        return value
    def __validate_manufacturer(self, value):
        if not isinstance(value, str):
            raise TypeError('Manufacturer must be a string')
        if not value:
            raise ValueError('Manufacturer cannot be empty')
        return value
    def __validate_date_of_arrival_in_warehouse(self, value):
        if not isinstance(value, str):
            raise TypeError('Date of Arrival must be a string')
        if not value:
            raise ValueError('Date of Arrival cannot be empty')
        return value

    def __str__(self):
        return (f"Name: {self.__name}, Quantity: {self.__quantity}, Price: {self.__price}, "
                f"Manufacturer: {self.__manufacturer}, Date: {self.__date_of_arrival_in_warehouse}")

com1 = UserCommodity('Laptop', 10, 30000, 'Dell', '2026-06-25')
com2 = UserCommodity('Mouse', 50, 500, 'Logitech', '2026-06-26')
com3 = UserCommodity('Keyboard', 30, 1500, 'HyperX', '2026-06-27')
com4 = UserCommodity('Monitor', 15, 30000, 'Samsung', '2026-06-28')
com5 = UserCommodity('Headphones', 20, 1200, 'Sony', '2026-06-29')
com6 = UserCommodity('Laptop', 20, 1200, 'Apple', '2026-06-30')

commodity_list = [com1, com2, com3, com4, com5, com6]
