# OOP.2
# Продавець
# Найменування
# Кількість
# Ціна
# Дата_продажу
#
# Визначити кількість товарів, проданих продавцем «Іванов», вивести відомості про них і визначити
# лити товар з максимальною вартістю.
# class Saler:
#     def __init__(self, saler,  name, quantity, price, dateofsale):
#         self.__saler = saler
#         self.__name = name
#         self.__quantity = quantity
#         self.__price = price
#         self.__dateofsale = dateofsale
#
#     @property
#     def saler(self):
#         return self.__saler
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def quantity(self):
#         return self.__quantity
#     @property
#     def price(self):
#         return self.__price
#     @property
#     def dateofsale(self):
#         return self.__dateofsale
#
#     @saler.setter
#     def saler(self, saler):
#         self.__saler = saler
#     @name.setter
#     def name(self, name):
#         self.__name = name
#     @quantity.setter
#     def quantity(self, quantity):
#         self.__quantity = quantity
#     @price.setter
#     def price(self, price):
#         self.__price = price
#     @dateofsale.setter
#     def dateofsale(self, dateofsale):
#         self.__dateofsale = dateofsale
#
#
#
# listofprod = [Saler('Іванов', 'телефон', 1, 10000, '10-06-26'),
#               Saler('Петров', 'ноутбук', 1, 40000, '11-06-26'),
#               Saler('Іванов', 'ip камера', 4, 9000, '12-06-26'),
#               Saler('Сорокін', 'телефон', 1, 11000, '13-06-26'),
#               Saler('Іванов', 'планшет', 1, 15000, '14-06-26'),]
#
#
# def maxprice(saler):
#     item_price = 0
#     print(saler)
#     for i in saler:
#         if i.price > item_price:
#             item_price = i.price
#
#
# def counting(listofprod, name):
#     saler = []
#     for i in listofprod:
#         if name == i.name:
#             saler.append(i)
#     if len(saler) == 0:
#         return 'Такого продавця не існує.'
#     else:
#         return maxprice(saler)
#
# sal = Saler.counting(listofprod, 'Іванов')
# print(sal)
'''
listofprod - це перелік товарів з вказанням продавця.
метод counting приймає цей перелік і імя яке потрібно знайти і передає новий список до метода maxprice
який виводить загальний список по продавцю і повертає максимальну продажу.
'''
from unittest import result

'''
OOP. 1
Автор
Кількість сторінок
Тираж
Рік видання
 
Вивести дані про книги, у яких кількість сторінок більша за 150
'''
class UserBooks:
    def __init__(self, author, count_pages, tirh, year):
        self.__author = author
        self.__count_pages = count_pages
        self.__tirh = tirh
        self.__year = year



    @property
    def author(self):
        return self.__author
    @property
    def count_pages(self):
        return self.__count_pages
    @property
    def tirh(self):
        return self.__tirh
    @property
    def year(self):
        return self.__year

    @author.setter
    def author(self, author):
        self.__author = author
    @count_pages.setter
    def count_pages(self, count_pages):
        self.__count_pages = count_pages
    @tirh.setter
    def tirh(self, tirh):
        self.__tirh = tirh
    @year.setter
    def year(self, year):
        self.__year = year

    def __str__(self):
        return f'{self.__author}, {self.__count_pages}, {self.__tirh}, {self.__year}'

list_of_books = [UserBooks('Марк Твен', 345, 20000, 1856),
                 UserBooks('Марко Вовчок', 120, 1000, 1956),
                 UserBooks('Марко Поло', 110, 10000, 1356),
                 UserBooks('J. Martin', 600, 100000, 1999)]

#print(list_of_books.__str__())       ?????????????????????????????????

# Вивести дані про книги, у яких кількість сторінок більша за 150
def info_about_books_where_count_pages_bigger_then(list_of_books, count_pages):
    list_result = []
    try:
        for book in list_of_books:
            if book.count_pages > count_pages:
                list_result.append(book)

    except TypeError:
        print('Ви ввели символ, введіть число.')

    return list_result

result = info_about_books_where_count_pages_bigger_then(list_of_books, "150")
for book in result:
    print(book)
#print(result)           ??????????????????????????????????
