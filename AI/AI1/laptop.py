class Laptop:
    def __init__(self, brand, screen_size, price, ram):
        self.__brand = self.__validate_brand(brand)
        self.__screen_size = self.__validate_screen_size(screen_size)
        self.__price = self.__validate_price(price)
        self.__ram = self.__validate_ram(ram)

    @property
    def brand(self):
        return self.__brand
    @property
    def screen_size(self):
        return self.__screen_size
    @property
    def price(self):
        return self.__price
    @property
    def ram(self):
        return self.__ram

    @brand.setter
    def brand(self, value):
        self.__brand = self.__validate_brand(value)
    @screen_size.setter
    def screen_size(self, value):
        self.__screen_size = self.__validate_screen_size(value)
    @price.setter
    def price(self, value):
        self.__price = self.__validate_price(value)
    @ram.setter
    def ram(self, value):
        self.__ram = self.__validate_ram(value)

    def __validate_brand(self, value):
        if not isinstance(value, str):
            raise ValueError("brand must be a string")
        value = value.strip()
        if not value:
            raise ValueError("brand cannot be empty")
        return value
    def __validate_screen_size(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("screen_size must be a number")
        if value <= 0:
            raise ValueError("screen_size must be greater than 0")
        return float(value)
    def __validate_price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("price must be a number")
        if value < 0:
            raise ValueError("price cannot be negative")
        return float(value)
    def __validate_ram(self, value):
        if not isinstance(value, int):
            raise ValueError("ram must be an integer")
        if value <= 0:
            raise ValueError("ram must be greater than 0")
        return value

    def __str__(self):
        return (
            f"Laptop(brand={self.brand}, screen_size={self.screen_size}, "
            f"price={self.price}, ram={self.ram})"
        )