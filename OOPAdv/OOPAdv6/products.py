class Product:
    def __init__(self, name, quantity, price, year_of_manufacture, manufacturer):
        self.__name =self.__validate_name(name)
        self.__quantity = self.__validate_quantity(quantity)
        self.__price = self.__validate_price(price)
        self.__year_of_manufacture = self.__validate_year_of_manufacture(year_of_manufacture)
        self.__manufacturer = self.__validate_manufacturer(manufacturer)

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
    def __validate_year_of_manufacture(self, value):
        if not isinstance(value, int):
            raise ValueError("year_of_manufacture must be an integer")
        if value < 1900 or value > 2026:
            raise ValueError("year_of_manufacture is invalid")
        return value
    def __validate_manufacturer(self, value):
        if not isinstance(value, str):
            raise ValueError("manufacturer must be a string")
        value = value.strip()
        if not value:
            raise ValueError("manufacturer cannot be empty")
        return value

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
    def year_of_manufacture(self):
        return self.__year_of_manufacture
    @property
    def manufacturer(self):
        return self.__manufacturer

    @name.setter
    def name(self, value):
        self.__name = self.__validate_name(value)
    @quantity.setter
    def quantity(self, value):
        self.__quantity = self.__validate_quantity(value)
    @price.setter
    def price(self, value):
        self.__price = self.__validate_price(value)
    @year_of_manufacture.setter
    def year_of_manufacture(self, value):
        self.__year_of_manufacture = self.__validate_year_of_manufacture(value)
    @manufacturer.setter
    def manufacturer(self, value):
        self.__manufacturer = self.__validate_manufacturer(value)

    def __str__(self):
        return (
            f"Product(name={self.name}, quantity={self.quantity}, "
            f"price={self.price}, year_of_manufacture={self.year_of_manufacture}, "
            f"manufacturer={self.manufacturer})"
        )

product1 = Product('Laptop', 10, 30000.00, 2026, 'Dell')
product2 = Product('Mouse', 50, 500.00, 2026, 'Logitech')
product3 = Product('Keyboard', 30, 1500.00, 2026, 'HyperX')
product4 = Product('Monitor', 15, 7000.00, 2025, 'Samsung')
product5 = Product('Headphones', 20, 1200.00, 2026, 'Sony')
product6 = Product('Webcam', 25, 2000.00, 2025, 'Logitech')

products_list = [product1, product2, product3, product4, product5, product6]