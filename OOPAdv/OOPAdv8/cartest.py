import unittest
import datetime
from car import Car
from car import cars_list
from carmethods import find_one_year


class TestsCar(unittest.TestCase):
    def setUp(self):
        self.list_obj = [Car("Toyota Camry", "Toyota Motor Corporation", "Седан", 2021, datetime.date(2025, 5, 10),
                             datetime.date(2025, 3, 15))]

    def test_count_of_rows(self):
        res = find_one_year(cars_list)
        self.assertEqual(len(res), 1)

    def test_isinstance_list(self):
        res = find_one_year(cars_list)
        self.assertIsInstance(res, list)


if __name__ == "__main__":
    unittest.main()