# Прізвище, рік народження, посада, зарплата, освіта
# Визначити наймолодшого працівника та надрукувати відомості про нього
from pathlib import Path

class Emploeeys:
    def __init__(self, last_name, year_of_birth, position, salary, education):
        self.__last_name = last_name
        self.__year_of_birth = year_of_birth
        self.__position = position
        self.__salary = salary
        self.__education = education

    @property
    def last_name(self):
        return self.__last_name
    @property
    def year_of_birth(self):
        return self.__year_of_birth
    @property
    def position(self):
        return self.__position
    @property
    def salary(self):
        return self.__salary
    @property
    def education(self):
        return self.__education

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
    @year_of_birth.setter
    def year_of_birth(self, year_of_birth):
        self.__year_of_birth = year_of_birth
    @position.setter
    def position(self, position):
        self.__position = position
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
    @education.setter
    def education(self, education):
        self.__education = education

    def __str__(self):
        return (f"Last name: {self.last_name}, Year of birth: {self.year_of_birth}, "
                f"Position: {self.position}, Salary: {self.salary}, "
                f"Education: {self.education}")

class Research:
    @classmethod
    def the_youngest_emp(cls, some_list):
        user_year = None
        for i in some_list:
            if user_year is None or i.year_of_birth > user_year.year_of_birth:
                user_year = i
        yield user_year

def writing_to_file(obj, file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f'Last name: {obj.last_name}, \nyear of birthday: {obj.year_of_birth}, \nposition: {obj.position}, \nsalary: {obj.salary}, \neducation: {obj.education}')
    except IOError:
        print('Якась помилка!!!')

def reading_to_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            f.read()
            for line in f:
                print(line)
    except IOError:
        print('Якась помилка!!!')

emploeey1 = Emploeeys("Ivanov", 1985, "Manager", 30000, "Higher")
emploeey2 = Emploeeys("Petrov", 1990, "Engineer", 35000, "Higher")
emploeey3 = Emploeeys("Sidorov", 1988, "Accountant", 28000, "Higher")
emploeey4 = Emploeeys("Brown", 1995, "Developer", 40000, "Higher")
emploeey5 = Emploeeys("Smith", 1982, "Director", 60000, "Higher")

emploeeys = [emploeey1, emploeey2, emploeey3, emploeey4, emploeey5]

#file_name_classwork = "C:\\Users\\khalt\\Documents\\JS\\pyCat\\CBS\\OOP\\OOP8\\classwork.txt"
file_name_classwork = Path(__file__).parent/"classwork.txt"

for i in Research.the_youngest_emp(emploeeys):
    print(i)
    writing_to_file(i, file_name_classwork)

reading_to_file(file_name_classwork)