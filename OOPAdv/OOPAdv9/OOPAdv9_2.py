# Взяти функцію розрахунку маси тіла з Python Starter українською/Домашнє_завдання 8/Завдання 5. Покрити її 10 тестами, щоб перевірити роботоздатність, використовуючи заздалегідь валідні дані та навпаки(введення текстових даних у поля, від'ємні значення тощо).
# За необхідності взяти її та доопрацювати до максимально стабільного варіанту.
# В процессі тестування використати:

# - оператор assert;
# - pytest;
# -unittest.
import unittest
import pytest

def u_func(a, b):
    res = b / (a ** 2)
    u_str = ''
    if res < 18.5:
        u_str = 'Недостатня вага.'
    elif 18.5 < res < 25.0:
        u_str = 'Масса тіла в нормі.'
    else:
        u_str = 'Слідкуйте за фігурою.'
    return res, u_str

res = u_func(1.8, 80)
print(res[0], res[1])

class UserTest(unittest.TestCase):
    def test_01_u_func(self):
        x = 1.8
        y = 80
        res = u_func(x, y)
        self.assertAlmostEqual(round(res[0]), 25)

    def test_02_result_is_tuple(self):
        result = u_func(1.8, 80)
        self.assertIsInstance(result, tuple)

    def test_03_u_func_true(self):
        x = 1.8
        y = 80
        res = u_func(x, y)
        self.assertTrue(round(res[0]) < 30)

    def test_04_u_func_zero(self):
        with self.assertRaises(ZeroDivisionError):
            u_func(0, 80)

    def test_05_u_func_less(self):
        x = 30
        y = 120
        res = u_func(x, y)
        self.assertLess(round(res[0]), 30)

def test_value_is_correct():
    result = u_func(2, 80)
    assert result[0] == 20.0

def test_is_float():
    result = u_func(1.8, 80)
    assert isinstance(result[0], float)

def test_is_positive():
    result = u_func(1.8, 80)
    assert result[0] > 0

def test_boundary_18_5():
    result = u_func(2, 74)
    assert result[0] == 18.5
    assert result[1] == 'Слідкуйте за фігурою.'

def test_zero_height_raises_error():
    with pytest.raises(ZeroDivisionError):
        u_func(0, 70)

# if __name__ == "__main__":
#     unittest.main()
"""Запускав тести через командний рядок.
    Перейшов в дерикторію з файлом.
    За допомогою запису py -m pytest -v OOPAdv9_2.py виконались всі десять тестів"""