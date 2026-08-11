# Попрацюйте зі створенням власних діалектів, довільно вибираючи правила для CSV-файлів. Зареєструйте створені
# діалекти та попрацюйте, використовуючи їх зі створенням/читанням файлом.
import csv
from pathlib import Path

file_path = Path(__file__).parent / "products.csv"

csv.register_dialect(
    "my_shop",
    delimiter=";",
    quotechar="'",
    quoting=csv.QUOTE_ALL,
    lineterminator="\n"
)

products = [
    ["Назва", "Ціна", "Категорія"],
    ["Ноутбук", 25000, "Комп'ютери"],
    ["Миша", 800, "Аксесуари"],
    ["Монітор", 12000, "Комп'ютери"]
]

# Запис даних у CSV-файл
with open(file_path, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, dialect="my_shop")
    writer.writerows(products)

print("CSV-файл створено.")

# Читання даних з CSV-файлу
with open(file_path, "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file, dialect="my_shop")

    print("\nДані з файлу:")
    for row in reader:
        print(row)