# Прізвище, група, рік народження, оцінка з фізики, оцінка з матеметики, оцінка з інформатики
# Last name, group, year of birth, physics_grade, mathematics_grade, computer_science_grade
# Надрукувати прізвища студентів, які склали математику на 95 і визначити їхню кількість
from pathlib import Path

class Student:
    def __init__(self, last_name, group, year_of_birth, physics_grade, mathematics_grade, computer_science_grade):
        self.__last_name = last_name
        self.__group = group
        self.__year_of_birth = year_of_birth
        self.__physics_grade = physics_grade
        self.__mathematics_grade = mathematics_grade
        self.__computer_science_grade = computer_science_grade

    @property
    def last_name(self):
        return self.__last_name
    @property
    def group(self):
        return self.__group
    @property
    def year_of_birth(self):
        return self.__year_of_birth
    @property
    def physics_grade(self):
        return self.__physics_grade
    @property
    def mathematics_grade(self):
        return self.__mathematics_grade
    @property
    def computer_science_grade(self):
        return self.__computer_science_grade

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
    @group.setter
    def group(self, group):
        self.__group = group
    @year_of_birth.setter
    def year_of_birth(self, year_of_birth):
        self.__year_of_birth = year_of_birth
    @physics_grade.setter
    def physics_grade(self, physics_grade):
        self.__physics_grade = physics_grade
    @mathematics_grade.setter
    def mathematics_grade(self, mathematics_grade):
        self.__mathematics_grade = mathematics_grade
    @computer_science_grade.setter
    def computer_science_grade(self, computer_science_grade):
        self.__computer_science_grade = computer_science_grade

    def __str__(self):
        return (f"Last name: {self.last_name}, Group: {self.group}, Year of birth: {self.year_of_birth}, "
                f"Physics grade: {self.physics_grade}, Mathematics grade: {self.mathematics_grade}, "
                f"Computer_science_grade: {self.computer_science_grade}")

class Research:
    def searching(self, some_list):
        result_list = []
        for i in some_list:
            if i.mathematics_grade == 95:
                result_list.append(i)
        return result_list

    def counting(self, some_list):
        count = 0
        for i in some_list:
            if i.mathematics_grade == 95:
                count += 1
        return count

def writing_to_file(obj, file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f'Last name: {obj.last_name}, group: {obj.group}, birthday: {obj.year_of_birth}, mathematics grade: {obj.mathematics_grade}') #
    except IOError:
        print('Якась помилка запису!!!')

def reading_to_file(file_name):
    try:
        with open(file_name, 'r', encoding="utf-8") as f:
            for line in f:
                print(line)
    except IOError:
        print('Якась помилка читання!!!')

student1 = Student("Ivanov", "P1", 1985, 60, 95, 60)
student2 = Student("Petrov", "P1", 1990, 65, 95, 65)
student3 = Student("Sidorov", "P1", 1988, 90, 70, 90)
student4 = Student("Brown", "P1", 1995, 80, 80, 80)
student5 = Student("Smith", "P1", 1982, 78, 60, 78)

students = [student1, student2, student3, student4, student5]

file_name_homework = Path(__file__).parent/"homework.txt"

r = Research()

print('Кількість студентів які склали математику на 95: ', r.counting(students))

g = r.searching(students)
for i in g:
    print(i)
    writing_to_file(i, file_name_homework)

reading_to_file(file_name_homework)