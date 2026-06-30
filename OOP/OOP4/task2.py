# Напишіть програму-калькулятор, яка підтримує такі операції: додавання, віднімання, множення, ділення
# та піднесення до ступеня. Програма має видавати повідомлення про помилку та продовжувати роботу під
# час введення некоректних даних, діленні на нуль та зведенні нуля в негативний степінь.
class UserCalculator:
    def __init__(self):  # , first_number, sign, second_number
        self.__first_number = None
        self.__sign = None
        self.__second_number = None

    @property
    def first_number(self):
        return self.__first_number

    @property
    def sign(self):
        return self.__sign

    @property
    def second_number(self):
        return self.__second_number

    @first_number.setter
    def first_number(self, first_number):
        self.__first_number = first_number

    @sign.setter
    def sign(self, sign):
        self.__sign = sign

    @second_number.setter
    def second_number(self, second_number):
        self.__second_number = second_number

    def calculations(self, first_number, sign, second_number):  #
        # res = 0
        match self.sign:
            case '+':
                return self.first_number + self.second_number
            case '-':
                return self.first_number - self.second_number
            case '*':
                return self.first_number * self.second_number
            case '/':
                try:
                    return self.first_number / self.second_number
                except ZeroDivisionError:
                    return 'Ви намагаєтесь поділити на ноль.'
            case '**':
                try:
                    return self.first_number ** self.second_number
                except ZeroDivisionError:
                    return "Ви намагаєтесь ноль підвести до від'ємного ступеня."
            case _:
                return 'Такаої дії покищо нема в цьому калькуляторі.'


calc = UserCalculator()
user_flag = True
print('Калькулятор вміє робити наступні дії: + - * / **')
print('Для того щоб вийти з прогруми калькулятора натисніть n або q')
while user_flag:
    if input('Бажаєте обрахувати?').lower() in ('n', 'q'):
        user_flag = False
        break
    calc.first_number = int(input('Введіть перше число: '))
    calc.sign = input('Введіть дію: ')
    calc.second_number = int(input('Введіть друге число: '))
    res = calc.calculations(calc.first_number, calc.sign, calc.second_number)
    print(res)