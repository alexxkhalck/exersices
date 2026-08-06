# Назва, кількість, ціна, рік виготовлення, виробник

# Визначити найдорожчий товар на складі та надрукувати всі відомості про нього

#from functools import reduce

class WarehouseItem:
    def __init__(self, name, quantity, price, manufacturer, date_of_arrival_in_warehouse):
        self.__name = self.__validate_name(name)
        self.__quantity = self.__validate_quantity(quantity)
        self.__price = self.__validate_price(price)
        self.__manufacturer = self.__validate_manufacturer(manufacturer)
        self.__date_of_arrival_in_warehouse = self.__validate_date_of_arrival(date_of_arrival_in_warehouse)

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
            raise ValueError("name must be a string")
        value = value.strip()
        if not value:
            raise ValueError("name cannot be empty")
        return value
    def __validate_quantity(self, value):
        if not isinstance(value, int):
            raise ValueError("quantity must be an integer")
        if value < 0:
            raise ValueError("quantity cannot be negative")
        return value
    def __validate_price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("price must be a number")
        if value < 0:
            raise ValueError("price cannot be negative")
        return float(value)
    def __validate_manufacturer(self, value):
        if not isinstance(value, str):
            raise ValueError("manufacturer must be a string")
        value = value.strip()
        if not value:
            raise ValueError("manufacturer cannot be empty")
        return value
    def __validate_date_of_arrival(self, value):
        if not isinstance(value, str):
            raise ValueError("date_of_arrival_in_warehouse must be a string in format DD.MM.YYYY")
        value = value.strip()
        if not value:
            raise ValueError("date_of_arrival_in_warehouse cannot be empty")
        return value

    def __str__(self):
        return (f"Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}, "
                f"Manufacturer: {self.manufacturer}, Date of arrival in warehouse: {self.date_of_arrival_in_warehouse}")

item1 = WarehouseItem('Laptop', 10, 7000, 'Dell', '2026-06-25')
item2 = WarehouseItem('Mouse', 50, 500, 'Logitech', '2026-06-26')
item3 = WarehouseItem('Keyboard', 30, 1500, 'HyperX', '2026-06-27')
item4 = WarehouseItem('Monitor', 15, 30000, 'Samsung', '2026-06-28')
item5 = WarehouseItem('Headphones', 20, 1200, 'Sony', '2026-06-29')

warehouse_items = [item1, item2, item3, item4, item5]

user_max = max(i.price for i in warehouse_items)
#finding_out_the_most_expansive = list(filter(lambda x: x.price == user_max, warehouse_items))

#print(str(finding_out_the_most_expansive))

for i in filter(lambda x: x.price == user_max, warehouse_items):
    print(i)