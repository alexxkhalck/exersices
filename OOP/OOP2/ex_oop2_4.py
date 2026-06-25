# Створіть UML-діаграми до завдань 1, 3 та 7. Збережіть їх у форматі *.uml.
# task 1
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def say_meow(self):
#         print(f"{self.name}: Meow!")
#
#
# class Kitty(Cat):
#     pass
#
#
# my_cat = Cat("Black")
# my_kitty = Kitty("Gray")
#
# my_cat.say_meow()
# my_kitty.say_meow()

# task 3
# class Bird:
# 	TYPE = "Bird"
#
# 	def fly(self):
# 		print(f"I am a {self.TYPE} and I can fly!")
#
#
# class Horse:
# 	TYPE = "Horse"
#
# 	def run(self):
# 		print(f"I am a {self.TYPE} and I can run!")
#
#
# class Pegas(Bird, Horse):
# 	pass
#
#
# my_home_pegas = Pegas()
# my_home_pegas.run()
# my_home_pegas.fly()

# task 7
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
#
# class Square(Rectangle):
#     def __init__(self, length):
#         # Для квадрата просто потрібно передати один параметр length.
#         # При виклику 'super().__init__()' встановимо атрибути 'length' та 'width'.
#         super().__init__(length, length)
#
#
# # Клас Square явно не реалізує метод area() і використовуватиме його із суперкласу Rectangle:
# sqr = Square(4)
# print("Area of Square is:", sqr.area())
#
# rect = Rectangle(2, 4)
# print("Area of Rectangle is:", rect.area())