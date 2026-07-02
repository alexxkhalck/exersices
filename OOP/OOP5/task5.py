# Використовуючи код завдання 2 надрукуйте у терміналі інформацію, яка міститься у класах Contact та
# UpdateContact та їх екземплярах. Видаліть атрибут job, і знову надрукуйте стан класів та їх екземплярів.
# Порівняйте їх. Зробіть відповідні висновки.
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

    @job.deleter
    def job(self):
        del self.__job

    def get_message(self):
        pass


con = Contact('Samov', 'Sam', 25, +123456788888, 'samsamov@gmail.com')
ucon = UpdateContact('Samov', 'Sam', 25, +123456788899, 'samsamov@gmail.com', 'manager')

print("Contact.__dict__:", Contact.__dict__)
print("UpdateContact.__dict__:", UpdateContact.__dict__)

print("Стан екземплярів ДО видалення job")
print("con.__dict__:", con.__dict__)
print("ucon.__dict__:", ucon.__dict__)

delattr(ucon, "job")
delattr(UpdateContact, "job")

print("Стан класів ПІСЛЯ видалення job")
print("Contact.__dict__:", Contact.__dict__)
print("UpdateContact.__dict__:", UpdateContact.__dict__)

print("Стан екземплярів ПІСЛЯ видалення job")
print("contact.__dict__:", con.__dict__)
print("ucon.__dict__:", ucon.__dict__)