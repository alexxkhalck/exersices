# Опишіть свій клас винятку. Напишіть функцію, яка викидатиме цей виняток, якщо користувач введе певне
# значення, і перехопіть цей виняток під час виклику функції.
class UserExeption:
    def __init__(self):
        self.__user_string = None

    @property
    def user_string(self):
        return self.__user_string

    @user_string.setter
    def user_string(self, user_string):
        self.__user_string = user_string

    def __str__(self):
        print(f'Ви ввели наступну строку: {self.user_string}')

    def user_exaption(self):
        try:
            u_str = input('Enter not empty string. ')
            if u_str.strip() == '':
                raise ValueError('Ви ввели порожній рядок.')
            self.user_string = u_str
            self.__str__()
        except ValueError as e:
            print(f'Ви ввели пусту строку. {e}')


ue = UserExeption()
ue.user_exaption()