# Для таблиці «матеріалу» з завдання 4 створіть функцію користувача, яка приймає необмежену кількість полів і
# повертає їх конкатенацію.
import sqlite3

def concatenate_fields(*args):
    return " | ".join(
        str(value)
        for value in args
        if value is not None
    )

connection = sqlite3.connect("materials.db")

connection.create_function(
    "CONCAT_FIELDS",
    -1,
    concatenate_fields
)

cursor = connection.cursor()

cursor.execute("""
    SELECT
        id,
        CONCAT_FIELDS(
            'Вага:', weight,
            'Висота:', height,
            'Характеристики:', characteristics
        ) AS material_info
    FROM materials
""")

materials = cursor.fetchall()

for material_id, material_info in materials:
    print(f"Матеріал ID {material_id}:")
    print(material_info)
    print()

connection.close()