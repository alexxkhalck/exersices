# Створити функцію, яка допоможе порахувати швидкість автомобіля. Набір даних, який використовується для розрахунку:
# * довжина шляху;
# * тривалість шляху.
# Створити 5-7 тестів використовуючи оператор assert.
import unittest

def car_speed(path_length: int, path_duration: int)->float:
    return path_length / path_duration * 60

#print(car_speed(60,10))

class UserTests(unittest.TestCase):
    def test_car_speed(self):
        x = 60
        y = 30
        self.assertAlmostEqual(car_speed(x, y), 120)

    def test_result_is_float(self):
        result = car_speed(60, 30)
        self.assertIsInstance(result, float)

    def test_car_speed_true(self):
        x = 60
        y = 30
        self.assertTrue(car_speed(x, y) > 100)

    def test_car_speed_zero(self):
        with self.assertRaises(ZeroDivisionError):
            car_speed(60, 0)

    def test_car_speed_less(self):
        x = 30
        y = 120
        self.assertLess(car_speed(x, y), 60)

if __name__ == "__main__":
    unittest.main()