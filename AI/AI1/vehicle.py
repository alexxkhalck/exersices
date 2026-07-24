class Vehicle:
    def __init__(self, brand, year, price, horsepower):
        self.__brand = self.__validate_brand(brand)
        self.__year = self.__validate_year(year)
        self.__price = self.__validate_price(price)
        self.__horsepower = self.__validate_horsepower(horsepower)

    @property
    def brand(self):
        return self.__brand
    @property
    def year(self):
        return self.__year
    @property
    def price(self):
        return self.__price
    @property
    def horsepower(self):
        return self.__horsepower

    @brand.setter
    def brand(self, value):
        self.__brand = self.__validate_brand(value)
    @year.setter
    def year(self, value):
        self.__year = self.__validate_year(value)
    @price.setter
    def price(self, value):
        self.__price = self.__validate_price(value)
    @horsepower.setter
    def horsepower(self, value):
        self.__horsepower = self.__validate_horsepower(value)

    def __validate_brand(self, value):
        if not isinstance(value, str):
            raise ValueError("brand must be a string")
        value = value.strip()
        if not value:
            raise ValueError("brand cannot be empty")
        return value
    def __validate_year(self, value):
        if not isinstance(value, int):
            raise ValueError("year must be an integer")
        if value < 1900 or value > 2026:
            raise ValueError("year is out of valid range")
        return value
    def __validate_price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("price must be a number")
        if value < 0:
            raise ValueError("price cannot be negative")
        return float(value)

    def __validate_horsepower(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("horsepower must be a number")
        if value <= 0:
            raise ValueError("horsepower must be greater than 0")
        return float(value)

    def __str__(self):
        return (
            f"Vehicle(brand={self.brand}, year={self.year}, "
            f"price={self.price}, horsepower={self.horsepower})"
        )