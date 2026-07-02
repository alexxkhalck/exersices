# Створити клас Contact з полями surname, name, age, mob_phone, email. Додати методи get_contact,
# sent_message. Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email, job.
# Додати методи get_message. Створити екземпляри класів та дослідити стан об'єктів за допомогою
# атрибутів: __dict__, __base__, __bases__. Роздрукувати інформацію на екрані.
class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.__surname = surname
        self.__name = name
        self.__age = age
        self.__mob_phone = mob_phone
        self.__email = email

    @property
    def surname(self):
        return self.__surname
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @property
    def mob_phone(self):
        return self.__mob_phone
    @property
    def email(self):
        return self.__email

    @surname.setter
    def surname(self, surname):
        self.__surname = surname
    @name.setter
    def name(self, name):
        self.__name = name
    @age.setter
    def age(self, age):
        self.__age = age
    @mob_phone.setter
    def mob_phone(self, mob_phone):
        self.__mob_phone = mob_phone
    @email.setter
    def email(self, email):
        self.__email = email

    def get_contact(salf):
        pass

    def sent_message(salf):
        pass


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.__surname = surname
        self.__name = name
        self.__age = age
        self.__mob_phone = mob_phone
        self.__email = email
        self.__job = job

    @property
    def surname(self):
        return self.__surname
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @property
    def mob_phone(self):
        return self.__mob_phone
    @property
    def email(self):
        return self.__email
    @property
    def job(self):
        return self.__job

    @surname.setter
    def surname(self, surname):
        self.__surname = surname
    @name.setter
    def name(self, name):
        self.__name = name
    @age.setter
    def age(self, age):
        self.__age = age
    @mob_phone.setter
    def mob_phone(self, mob_phone):
        self.__mob_phone = mob_phone

    @email.setter
    def email(self, email):
        self.__email = email
    @job.setter
    def job(self, job):
        self.__job = job

    def get_message(self):
        pass


con = Contact('Samov', 'Sam', 25, +123456788888, 'samsamov@gmail.com')
ucon = UpdateContact('Samov', 'Sam', 25, +123456788899, 'samsamov@gmail.com', 'manager')

print('Словник: ', con.__dict__)
print('Батьківський класс: ', Contact.__base__)
print('Всі батьківські класси: ', Contact.__bases__)
print()
print()
print('Словник: ', ucon.__dict__)
print('Батьківський класс: ', UpdateContact.__base__)
print('Всі батьківські класси: ', UpdateContact.__bases__)

# surname, name, age, mob_phone, email