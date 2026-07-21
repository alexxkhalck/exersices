# прізвище ім'я по батькові посада зарплата дата народження
# Вивести відомості про працівників, у яких зп вища за середню і вік менший 30 років.
# lastname firstname middlename position salary date_of_birth
class Employee:
    def __init__(self, lastname, firstname, middlename, position, salary, date_of_birth):
        self.__lastname = self.__validate_lastname(lastname)
        self.__firstname = self.__validate_firstname(firstname)
        self.__middlename = self.__validate_middlename(middlename)
        self.__position = self.__validate_position(position)
        self.__salary = self.__validate_salary(salary)
        self.__date_of_birth = self.__validate_date_of_birth(date_of_birth)

    @property
    def lastname(self):
        return self.__lastname
    @property
    def firstname(self):
        return self.__firstname
    @property
    def middlename(self):
        return self.__middlename
    @property
    def position(self):
        return self.__position
    @property
    def salary(self):
        return self.__salary
    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @lastname.setter
    def lastname(self, value):
        self.__lastname = self.__validate_lastname(value)
    @firstname.setter
    def firstname(self, value):
        self.__firstname = self.__validate_firstname(value)
    @middlename.setter
    def middlename(self, value):
        self.__middlename = self.__validate_middlename(value)
    @position.setter
    def position(self, value):
        self.__position = self.__validate_position(value)
    @salary.setter
    def salary(self, value):
        self.__salary = self.__validate_salary(value)
    @date_of_birth.setter
    def date_of_birth(self, value):
        self.__date_of_birth = self.__validate_date_of_birth(value)

    def __validate_lastname(self, value):
        if not isinstance(value, str):
            raise ValueError("lastname must be a string")
        value = value.strip()
        if not value:
            raise ValueError("lastname cannot be empty")
        return value

    def __validate_firstname(self, value):
        if not isinstance(value, str):
            raise ValueError("firstname must be a string")
        value = value.strip()
        if not value:
            raise ValueError("firstname cannot be empty")
        return value

    def __validate_middlename(self, value):
        if not isinstance(value, str):
            raise ValueError("middlename must be a string")
        value = value.strip()
        if not value:
            raise ValueError("middlename cannot be empty")
        return value

    def __validate_position(self, value):
        if not isinstance(value, str):
            raise ValueError("position must be a string")
        value = value.strip()
        if not value:
            raise ValueError("position cannot be empty")
        return value

    def __validate_salary(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("salary must be a number")
        if value < 0:
            raise ValueError("salary cannot be negative")
        return float(value)

    def __validate_date_of_birth(self, value):
        if not isinstance(value, str):
            raise ValueError("date_of_birth must be a string in format DD.MM.YYYY")
        value = value.strip()
        if not value:
            raise ValueError("date_of_birth cannot be empty")
        return value

    def __str__(self):
        return (
            f"Employee(lastname={self.lastname}, firstname={self.firstname}, "
            f"middlename={self.middlename}, position={self.position}, "
            f"salary={self.salary}, date_of_birth={self.date_of_birth})"
        )