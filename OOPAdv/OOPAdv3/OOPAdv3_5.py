# Для таблиці «матеріалу» з завдання 4 створіть користувальницьку агрегатну функцію, яка рахує середнє значення ваги
# всіх матеріалів вислідної вибірки й округляє значення до цілого.
import sqlite3

class RoundedAverageWeight:
    def __init__(self):
        self.total_weight = 0
        self.count = 0

    def step(self, weight):
        if weight is not None:
            self.total_weight += weight
            self.count += 1

    def finalize(self):
        if self.count == 0:
            return None

        average = self.total_weight / self.count
        return round(average)

connection = sqlite3.connect("materials.db")

connection.create_aggregate(
    "ROUND_AVG_WEIGHT",
    1,
    RoundedAverageWeight
)

cursor = connection.cursor()

cursor.execute("""
    SELECT ROUND_AVG_WEIGHT(weight)
    FROM materials
""")

result = cursor.fetchone()[0]

print(f"Середня вага матеріалів: {result}")

connection.close()