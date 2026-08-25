# Визначити кількість працівників-інженерів і надрукувати всі відомості про них. Визначити найстаршого та наймолодшого працівника.
# Зробити двома способами: звичайною функцією та лямбдою.

class Employee:
    def __init__(self, lastname, birthday, salary, position, education):
        self.__lastname = self.__validate_lastname(lastname)
        self.__birthday = self.__validate_birthday(birthday)
        self.__salary = self.__validate_salary(salary)
        self.__position = self.__validate_position(position)
        self.__education = self.__validate_education(education)

    def __validate_lastname(self, lastname):
        if not isinstance(lastname, str):
            raise TypeError("Прізвище повинно бути рядком.")

        lastname = lastname.strip()

        if not lastname:
            raise ValueError("Прізвище не може бути порожнім.")

        return lastname

    def __validate_birthday(self, birthday):
        if not isinstance(birthday, int):
            raise TypeError(
                "Дата народження повинна бути об'єктом date."
            )
        return birthday

    def __validate_salary(self, salary):
        if not isinstance(salary, int):
            raise TypeError("Зарплати повинні бути списком.")

        if not salary:
            raise ValueError("Список зарплат не може бути порожнім.")

        if (not isinstance(salary, int) or isinstance(salary, bool) or salary < 0):
            raise ValueError(
                "Зарплата повинна бути невід'ємним числом."
            )

        return salary

    def __validate_position(self, position):
        if not isinstance(position, str):
            raise TypeError("Посада повинна бути рядком.")

        position = position.strip()

        if not position:
            raise ValueError("Посада не може бути порожньою.")

        return position

    def __validate_education(self, education):
        if not isinstance(education, str):
            raise TypeError("Освіта повинна бути рядком.")

        education = education.strip()

        if not education:
            raise ValueError("Освіта не може бути порожньою.")

        return education

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = self.__validate_lastname(lastname)

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = self.__validate_birthday(birthday)

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = self.__validate_salary(salary)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = self.__validate_position(position)

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, education):
        self.__education = self.__validate_education(education)

    def __str__(self):
        return (f"Employee(lastname='{self.__lastname}', birthday={self.__birthday}, "
            f"salary={self.__salary}, position='{self.__position}', education='{self.__education}')")

employee1 = Employee("Шевченко", 1990, 30000, "Python Developer", "Вища технічна освіта")
employee2 = Employee("Коваленко", 1988, 37000, "Backend Developer", "Магістр комп'ютерних наук")
employee3 = Employee("Бондаренко", 1995, 27000, "Engineer", "Вища освіта в галузі IT")
employee4 = Employee("Мельник", 1985, 45000, "Team Lead", "Магістр програмної інженерії")
employee5 = Employee("Ткаченко", 1998, 23000, "Junior Developer", "Незакінчена вища освіта")
employee6 = Employee("Олійник", 1992, 34000, "Engineer", "Магістр прикладної математики")

employees_list = [employee1, employee2, employee3, employee4, employee5, employee6]