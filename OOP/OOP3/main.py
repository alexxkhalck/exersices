# OOP.2
# Продавець
# Найменування
# Кількість
# Ціна
# Дата_продажу
#
# Визначити кількість товарів, проданих продавцем «Іванов», вивести відомості про них і визначити
# лити товар з максимальною вартістю.
class Saler:
    def __init__(self, saler,  name, quantity, price, dateofsale):
        self.__saler = saler
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__dateofsale = dateofsale

    @property
    def saler(self):
        return self.__saler
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
    def dateofsale(self):
        return self.__dateofsale

    @saler.setter
    def saler(self, saler):
        self.__saler = saler
    @name.setter
    def name(self, name):
        self.__name = name
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
    @price.setter
    def price(self, price):
        self.__price = price
    @dateofsale.setter
    def dateofsale(self, dateofsale):
        self.__dateofsale = dateofsale

    @classmethod#staticmethod
    def maxprice(self, saler):
        item_price = 0
        print(saler)
        for i in saler:
            if i.price > item_price:
                item_price = i.price

    @classmethod
    def counting(listofprod, name):
        saler = []
        for i in listofprod:
            if name == i.name:
                saler.append(i)
        if len(saler) == 0:
            return 'Такого продавця не існує.'
        else:
            return maxprice(saler)

listofprod = [Saler('Іванов', 'телефон', 1, 10000, '10-06-26'),
              Saler('Петров', 'ноутбук', 1, 40000, '11-06-26'),
              Saler('Іванов', 'ip камера', 4, 9000, '12-06-26'),
              Saler('Сорокін', 'телефон', 1, 11000, '13-06-26'),
              Saler('Іванов', 'планшет', 1, 15000, '14-06-26'),]

sal = Saler.counting(listofprod, 'Іванов')
print(sal)
'''
listofprod - це перелік товарів з вказанням продавця.
метод counting приймає цей перелік і імя яке потрібно знайти і передає новий список до метода maxprice
який виводить загальний список по продавцю і повертає максимальну продажу.
'''