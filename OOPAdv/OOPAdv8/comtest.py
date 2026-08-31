import unittest
import datetime
from commodity import Commodity
from commethods import search_expiration_com

class EmpTest(unittest.TestCase):
    def setUp(self):
        self.year = datetime.date.today().year

    def test_expiration(self):
        commodity = [Commodity("something", 100.00, datetime.date.today(), datetime.date(2026, 8, 1), 10, "something")]
        self.assertEqual(search_expiration_com(commodity), 1000.00)

    def test_no_expiration(self):
        commodity = [Commodity("something", 100.00, datetime.date.today(), datetime.date(2026, 9, 1), 10, "something")]
        self.assertEqual(search_expiration_com(commodity), 0)

    def test_empty_list(self):
        self.assertEqual(search_expiration_com([]), 0)

if __name__ == "__main__":
    unittest.main()