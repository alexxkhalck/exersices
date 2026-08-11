# Створіть таблицю «матеріали» з таких полів: ідентифікатор, вага, висота та додаткові характеристики матеріалу.
# Поле «додаткові  характеристики матеріалу» має зберігати у собі масив, кожен елемент якого є кортежем із двох значень:
# перше – назва характеристики, а друге – її значення.
import sqlite3
import json

connection = sqlite3.connect("materials.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS materials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        weight REAL NOT NULL,
        height REAL NOT NULL,
        characteristics TEXT NOT NULL
    )
""")

connection.commit()

material_characteristics = [
    ("color", "red"),
    ("material", "steel"),
    ("waterproof", True),
    ("manufacturer", "Metal Company")
]

characteristics_json = json.dumps(
    material_characteristics,
    ensure_ascii=False
)

cursor.execute("""
    INSERT INTO materials (weight, height, characteristics)
    VALUES (?, ?, ?)
""", (
    15.5,
    120.0,
    characteristics_json
))

connection.commit()

print("Матеріал успішно додано.")

cursor.execute("""
    SELECT id, weight, height, characteristics
    FROM materials
""")

materials = cursor.fetchall()

for material_id, weight, height, characteristics_json in materials:
    characteristics = json.loads(characteristics_json)

    print(f"\nID: {material_id}")
    print(f"Вага: {weight}")
    print(f"Висота: {height}")
    print("Додаткові характеристики:")

    for name, value in characteristics:
        print(f"- {name}: {value}")

connection.close()