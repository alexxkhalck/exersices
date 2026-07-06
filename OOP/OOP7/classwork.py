# list_ = [x ** 2 for x in range(4)]
# print(list_)
# generator = (x ** 2 for x in range(4))
# list_ = generator
#
# print(list(list_))
# print(list(generator))
# Прізвище
# Вік
# Кількість ігор
# Кількість пропущених шайб
#
# Визначити середній вік хокеїстів і вивести відомості про хокеїстів вік яких понад 25 років.
# from collections.abc import Generator


# class Player:
#     def __init__(self, last_name, age, number_of_games, number_of_goals):
#         self.__last_name = last_name
#         self.__age = age
#         self.__number_of_games = number_of_games
#         self.__number_of_goals = number_of_goals

#     @property
#     def last_name(self):
#         return self.__last_name
#     @property
#     def age(self):
#         return self.__age
#     @property
#     def number_of_games(self):
#         return self.__number_of_games
#     @property
#     def number_of_goals(self):
#         return self.__number_of_goals

#     @last_name.setter
#     def last_name(self, last_name):
#         self.__last_name = last_name
#     @age.setter
#     def age(self, age):
#         self.__age = age
#     @number_of_games.setter
#     def number_of_games(self, number_of_games):
#         self.__number_of_games = number_of_games
#     @number_of_goals.setter
#     def number_of_goals(self, number_of_goals):
#         self.__number_of_goals = number_of_goals

#     def __str__(self):
#         return (f"Last name: {self.last_name}, Age: {self.age}, "
#                 f"Number of games: {self.number_of_games}, "
#                 f"Number of goals: {self.number_of_goals}")

# class MiddleAge:
#     @classmethod
#     def middle_age(cls, some_list):
#         generator = (item for item in some_list)
#         res = 0
#         for item in generator:
#             res += item.age
#         print('Середній вік хоккеїстів:', (res/len(some_list)))

#     #@classmethod
#     def players_25(cls, some_list):
#         for item in some_list:
#             if item.age >= 25:
#                 yield item


# player1 = Player('Ivanov', 20, 15, 5)
# player2 = Player('Petrov', 22, 30, 12)
# player3 = Player('Sidorov', 25, 10, 3)
# player4 = Player('Smith', 25, 40, 20)
# player5 = Player('Brown', 21, 25, 9)
# player6 = Player('Kovalenko', 23, 35, 17)

# players = [player1, player2, player3, player4, player5, player6]

# ma = MiddleAge()
# ma.middle_age(players)
# g = ma.players_25(players)
# for ret in g:
#     print(ret)
# Найменування
# Кількість
# Ціна
# Виробник
# Дата_випуску

# Визначити середню вартість товарів і товар мінімальною вартістю.
# class Product:
#     def __init__(self, name, quantity, price, manufacturer, release_date):
#         self.__name = name
#         self.__quantity = quantity
#         self.__price = price
#         self.__manufacturer = manufacturer
#         self.__release_date = release_date

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
#     def manufacturer(self):
#         return self.__manufacturer
#     @property
#     def release_date(self):
#         return self.__release_date

#     @name.setter
#     def name(self, name):
#         self.__name = name
#     @quantity.setter
#     def quantity(self, quantity):
#         self.__quantity = quantity
#     @price.setter
#     def price(self, price):
#         self.__price = price
#     @manufacturer.setter
#     def manufacturer(self, manufacturer):
#         self.__manufacturer = manufacturer
#     @release_date.setter
#     def release_date(self, release_date):
#         self.__release_date = release_date

#     def __str__(self):
#         return (f"Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}, "
#                 f"Manufacturer: {self.manufacturer}, Release date: {self.release_date}")

# class ProductReserch:
#     @classmethod
#     def middle_price(cls, some_list):
#         res = 0
#         for item in some_list:
#             res += item.price
#         return res / len(some_list)

#     @classmethod
#     def min_price(cls, some_list):
#         res = some_list[0].price
#         for item in some_list:
#             if item.price < res:
#                 res = item.price
#         return res

#     @classmethod
#     def date_release(cls, some_list):
#         for item in some_list:
#             if item.release_date == '2026':
#                 yield item

# product1 = Product('Laptop', 10, 30000, 'Dell', '2026')
# product2 = Product('Mouse', 50, 500, 'Logitech', '2026')
# product3 = Product('Keyboard', 30, 1500, 'HyperX', '2026')
# product4 = Product('Monitor', 15, 7000, 'Samsung', '2025')
# product5 = Product('Headphones', 20, 1200, 'Sony', '2026')
# product6 = Product('Webcam', 25, 2000, 'Logitech', '2025')

# products = [product1, product2, product3, product4, product5, product6]

# pr = ProductReserch()
# print('Середня ціна: ', pr.middle_price(products))
# print('Мінімальна ціна: ', pr.min_price(products))
# # Окремо для тренування генератора - за датою випуску
# gen = pr.date_release(products)
# for g in gen:
#     print(g)