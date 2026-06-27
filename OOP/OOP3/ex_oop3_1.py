# Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані?
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).
class Car:
    def __init__(self, mark, model, year, color, price, saler):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__color = color
        self.__price = price
        self.__saler = saler

    @property
    def mark(self):
        return self.__mark
    @property
    def model(self):
        return self.__model
    @property
    def year(self):
        return self.__year
    @property
    def color(self):
        return self.__color
    @property
    def price(self):
        return self.__price
    @property
    def saler(self):
        return self.__saler

    @mark.setter
    def mark(self, mark):
        if mark not in (None, ''):
            self.__mark = mark
    @model.setter
    def model(self, model):
        if model not in (None, ''):
            self.__model = model
    @year.setter
    def year(self, year):
        if year not in (None, ''):
            self.__year = year
    @color.setter
    def color(self, color):
        if color not in (None, ''):
            self.__color = color
    @price.setter
    def price(self, price):
        if price not in (None, 0):
            self.__price = price
    @saler.setter
    def saler(self, saler):
        if saler not in (None, ''):
            self.__saler = saler