class Laptop:
    def __init__(self, brand, screen_size, price, ram):
        self.__validate_brand(brand)
        self.__validate_screen_size(screen_size)
        self.__validate_price(price)
        self.__validate_ram(ram)

    # ---------- Приватні валідатори ----------

    def __validate_brand(self, brand):
        if not isinstance(brand, str):
            raise TypeError("Бренд повинен бути рядком.")
        if not brand.strip():
            raise ValueError("Бренд не може бути порожнім.")
        self.__brand = brand
    def __validate_screen_size(self, screen_size):
        if not isinstance(screen_size, (int, float)):
            raise TypeError("Діагональ повинна бути числом.")
        if screen_size <= 0:
            raise ValueError("Діагональ повинна бути більшою за 0.")
        self.__screen_size = screen_size
    def __validate_price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Ціна повинна бути числом.")
        if price <= 0:
            raise ValueError("Ціна повинна бути більшою за 0.")
        self.__price = price
    def __validate_ram(self, ram):
        if not isinstance(ram, int):
            raise TypeError("RAM повинен бути цілим числом.")
        if ram <= 0:
            raise ValueError("RAM повинен бути більшим за 0.")
        self.__ram = ram

    # ---------- Властивості ----------

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, value):
        self.__validate_brand(value)

    @property
    def screen_size(self):
        return self.__screen_size
    @screen_size.setter
    def screen_size(self, value):
        self.__validate_screen_size(value)

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        self.__validate_price(value)

    @property
    def ram(self):
        return self.__ram
    @ram.setter
    def ram(self, value):
        self.__validate_ram(value)

    def __str__(self):
        return (
            f"Laptop("
            f"brand='{self.__brand}', "
            f"screen_size={self.__screen_size}\", "
            f"price=${self.__price}, "
            f"ram={self.__ram} GB)"
        )