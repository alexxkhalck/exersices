import unittest
import datetime
from employees import Employee
from empmethods import finding_60_65

class EmpTest(unittest.TestCase):
    def setUp(self):
        self.year = datetime.date.today().year

    def test_male_over_65(self):
        employees = [
            Employee("somebudy", "somebudy", "somebudy", "somebudy", "male", datetime.date(self.year - 66, 1, 1))]
        self.assertEqual(finding_60_65(employees), 1)

    def test_male_under_65(self):
        employees = [
            Employee("somebudy", "somebudy", "somebudy", "somebudy", "male", datetime.date(self.year - 64, 1, 1))]
        self.assertEqual(finding_60_65(employees), 0)

    def test_female_over_60(self):
        employees = [
            Employee("somebudy", "somebudy", "somebudy", "somebudy", "female", datetime.date(self.year - 61, 1, 1))]
        self.assertEqual(finding_60_65(employees), 1)

    def test_female_under_60(self):
        employees = [
            Employee("somebudy", "somebudy", "somebudy", "somebudy", "female", datetime.date(self.year - 59, 1, 1))]
        self.assertEqual(finding_60_65(employees), 0)

    def test_empty_list(self):
        self.assertEqual(finding_60_65([]), 0)

if __name__ == "__main__":
    unittest.main()