# Кількість, ціна, рік виготовлення, виробник
# Визначити товар, кількість якого найбільша на складі, і надрукувати всі відомості про нього.
class ProductInfo:
    def __init__(self, quantity, price, year_of_manufacture, manufacturer):
        self.__quantity = quantity                 # захищене поле
        self.__price = price                       # захищене поле
        self.__year_of_manufacture = year_of_manufacture  # захищене поле
        self.__manufacturer = manufacturer         # захищене поле

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

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
    @price.setter
    def price(self, price):
        self.__price = price
    @year_of_manufacture.setter
    def year_of_manufacture(self, year_of_manufacture):
        self.__year_of_manufacture = year_of_manufacture
    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def __str__(self):
        return (f"Quantity: {self.quantity}, Price: {self.price}, "
                f"Year of manufacture: {self.year_of_manufacture}, "
                f"Manufacturer: {self.manufacturer}")