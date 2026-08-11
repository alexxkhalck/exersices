# Створіть функцію, яка формує CSV-файл на основі даних, введених користувачем через консоль. Файл має містити такі
# стовпчики: імена, прізвища, дати народження та місто проживання. Реалізуйте можливості перезапису цього файлу,
# додавання нових рядків до наявного файлу, рядкового читання з файлу та конвертації всього вмісту у формати XML та JSON.
import csv
import json
from pathlib import Path
import xml.etree.ElementTree as ET

BASE_PATH = Path(__file__).parent

CSV_FILE = BASE_PATH / "people.csv"
JSON_FILE = BASE_PATH / "people.json"
XML_FILE = BASE_PATH / "people.xml"

FIELDS = [
    "first_name",
    "last_name",
    "birth_date",
    "city"
]

def get_person_from_console():
    print("\nВведіть дані людини:")

    return {
        "first_name": input("Ім'я: ").strip(),
        "last_name": input("Прізвище: ").strip(),
        "birth_date": input("Дата народження (ДД.ММ.РРРР): ").strip(),
        "city": input("Місто проживання: ").strip()
    }

def overwrite_csv():
    person = get_person_from_console()

    with open(CSV_FILE, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerow(person)

    print("CSV-файл створено або перезаписано.")

def append_to_csv():
    person = get_person_from_console()

    file_exists = CSV_FILE.exists()
    file_is_empty = not file_exists or CSV_FILE.stat().st_size == 0

    with open(CSV_FILE, "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if file_is_empty:
            writer.writeheader()

        writer.writerow(person)

    print("Новий рядок додано до CSV-файлу.")

def read_csv_line_by_line():
    if not CSV_FILE.exists():
        print("Файл people.csv ще не створено.")
        return

    with open(CSV_FILE, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        print("\nВміст CSV-файлу:")

        for number, person in enumerate(reader, start=1):
            print(
                f"{number}. "
                f"{person['first_name']} "
                f"{person['last_name']}, "
                f"дата народження: {person['birth_date']}, "
                f"місто: {person['city']}"
            )

def load_people_from_csv():
    if not CSV_FILE.exists():
        print("Файл people.csv ще не створено.")
        return []

    with open(CSV_FILE, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def convert_csv_to_json():
    people = load_people_from_csv()

    if not people:
        return

    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(people, file, ensure_ascii=False, indent=4)

    print("Дані конвертовано у people.json.")

def convert_csv_to_xml():
    people = load_people_from_csv()

    if not people:
        return

    root = ET.Element("people")

    for person in people:
        person_element = ET.SubElement(root, "person")

        for field, value in person.items():
            field_element = ET.SubElement(person_element, field)
            field_element.text = value

    tree = ET.ElementTree(root)

    ET.indent(tree, space="    ")

    tree.write(
        XML_FILE,
        encoding="utf-8",
        xml_declaration=True
    )

    print("Дані конвертовано у people.xml.")

def show_menu():
    print("""
1 — Створити / перезаписати CSV-файл
2 — Додати новий запис у CSV-файл
3 — Прочитати CSV-файл построково
4 — Конвертувати CSV у JSON
5 — Конвертувати CSV у XML
0 — Вийти
""")

def main():
    while True:
        show_menu()
        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            overwrite_csv()

        elif choice == "2":
            append_to_csv()

        elif choice == "3":
            read_csv_line_by_line()

        elif choice == "4":
            convert_csv_to_json()

        elif choice == "5":
            convert_csv_to_xml()

        elif choice == "0":
            print("Програму завершено.")
            break

        else:
            print("Невірний пункт меню. Спробуйте ще раз.")

if __name__ == "__main__":
    main()