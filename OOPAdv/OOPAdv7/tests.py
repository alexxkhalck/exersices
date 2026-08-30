import unittest
from merch import Merchandice
from meth import average_cost
from meth import names_and_costs
# якщо я передам в клас TestMerchandice справжній список це буде ефективніше ніж створювати

class UserTests(unittest.TestCase):
    def setUp(self):
        self.items = [
            Merchandice("Apple", 1000.00),
            Merchandice("Груша", 2000.00),
            Merchandice("Слива", 3000.00),
        ]

    def test_average_cost(self):
        result = average_cost(self.items)
        #self.assertAlmostEqual(result, 2000.0)
        self.assertEqual(type(result), float)

    def test_average_cost_empty(self):
        with self.assertRaises(ZeroDivisionError):
            average_cost([])

    def test_names_and_costs(self):
        result = names_and_costs(self.items)
        expected = [("Apple", 1000.0), ("Груша", 2000.0), ("Слива", 3000.0)]
        self.assertEqual(result, expected)
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()