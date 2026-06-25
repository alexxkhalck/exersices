# Використовуючи код example_10, створіть декоратори @classmethod для формування переліку об'єктів,
# які підрахують кількість повнолітніх людей в Україні та Америці.
from datetime import date

class MyClass1:
    people = []

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age
        MyClass1.people.append(self)

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))

    @classmethod
    def count_adults_ukraine(cls):
        count = 0
        for person in cls.people:
            if person.age >= 18:
                count += 1
        return count

    @classmethod
    def count_adults_usa(cls):
        count = 0
        for person in cls.people:
            if person.age >= 21:
                count += 1
        return count


class MyClass2(MyClass1):
    color = 'White'


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan', 2000)
m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)

print('Повнолітні в Україні:', MyClass1.count_adults_ukraine())
print('Повнолітні в Америці:', MyClass1.count_adults_usa())