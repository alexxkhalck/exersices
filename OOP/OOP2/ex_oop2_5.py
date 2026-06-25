# Використовуючи код example_10, створіть декоратор @staticmethod для визначення повноліття людини
# в Україні та Америки.
from datetime import date

class MyClass1:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))

    @staticmethod
    def is_adult_ukraine(age):
        return age >= 18

    @staticmethod
    def is_adult_usa(age):
        return age >= 21

class MyClass2(MyClass1):
    color = 'White'


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per1.print_info()

print(MyClass1.is_adult_ukraine(m_per1.age))
print(MyClass1.is_adult_usa(m_per1.age))

m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan',  2000)
m_per2.print_info()

print(MyClass1.is_adult_ukraine(m_per2.age))
print(MyClass1.is_adult_usa(m_per2.age))

m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
print(isinstance(m_per3, MyClass2))

m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)
print(isinstance(m_per4, MyClass1))

print(issubclass(MyClass1, MyClass2))
print(issubclass(MyClass2, MyClass1))
