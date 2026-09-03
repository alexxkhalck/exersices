import unittest
from OOPAdv9_3 import Student

students_list = [
    Student('Іван', 'Петренко', 18, 92.5),
    Student('Олена', 'Коваль', 19, 88.0),
    Student('Андрій', 'Шевченко', 20, 76.5),
    Student('Марія', 'Бондаренко', 18, 95.0),
    Student('Максим', 'Мельник', 21, 81.5),
    Student('Софія', 'Ткаченко', 19, 99.0),
    Student('Дмитро', 'Кравченко', 22, 70.0),
    Student('Анна', 'Олійник', 20, 84.5),
    Student('Владислав', 'Романенко', 18, 90.0),
    Student('Катерина', 'Лисенко', 21, 78.0)
]

class UserTest(unittest.TestCase):
    def test_is_it_Student(self):
        for item in students_list:
            self.assertIsInstance(item, Student)

    def test_is_this_ten(self):
        self.assertEqual(len(students_list), 10)

    def test_max_grade_point(self):
        max_gps = max(item.gradepointaverage for item in students_list)
        self.assertEqual(max_gps, 99.0)

    def test_min_grade_point(self):
        min_gps = min(item.gradepointaverage for item in students_list)
        self.assertEqual(min_gps, 70.0)

if __name__ == "__main__":
    unittest.main()