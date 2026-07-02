# Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr().
# Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.
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

    @surname.deleter
    def surname(self):
        del self.__surname
    @name.deleter
    def name(self):
        del self.__name
    @age.deleter
    def age(self):
        del self.__age
    @mob_phone.deleter
    def mob_phone(self):
        del self.__mob_phone
    @email.deleter
    def email(self):
        del self.__email
    @job.deleter
    def job(self):
        del self.__job

    def get_message(self):
        pass


# con = Contact('Samov', 'Sam', 25, +123456788888, 'samsamov@gmail.com')
ucon = UpdateContact('Samov', 'Sam', 25, +123456788899, 'samsamov@gmail.com', 'manager')

print('Не існуючий атрибут', hasattr(ucon, 'middlename'))
print('Існуючий атрибут', hasattr(ucon, 'surname'))
print('Зміст атрибуту', getattr(ucon, 'surname'))
print('Заповнення атрибуту', setattr(ucon, 'surname', 'Семов'))
print('Зміст атрибуту після заповнення', getattr(ucon, 'surname'))
print('Видалення атрибуту', delattr(ucon, 'surname'))
print('Видалений атрибут', hasattr(ucon, 'surname'))

# hasattr(), getattr(), setattr(), delattr()