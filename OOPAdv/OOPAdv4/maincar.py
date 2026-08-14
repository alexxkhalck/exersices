import sqlite3
from pathlib import Path
from car import list_cars

file_db = Path(__file__).parent/"cars_db.db"

def create_db():
    connection = None
    try:
        create_table = '''CREATE TABLE IF NOT EXISTS cars_table(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            car_brand TEXT NOT NULL,
                            manufacturer TEXT NOT NULL,
                            car_type TEXT NOT NULL,
                            year_of_manufacture INTEGER NOT NULL,
                            registration_date INTEGER NOT NULL);'''
        connection = sqlite3.connect(file_db)
        cursor = connection.cursor()
        cursor.execute(create_table)
        connection.commit()
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()
            print("З'єднання з SQLite закрито")

def insert_rows_into_db(some_list):
    connection = None
    try:
        create_table = '''INSERT INTO cars_table
                            (car_brand, manufacturer, car_type, year_of_manufacture, registration_date)
                            VALUES (?,?,?,?,?);'''
        connection = sqlite3.connect(file_db)
        cursor = connection.cursor()
        for item in some_list:
            data_for_db = (item.car_brand, item.manufacturer, item.car_type, item.year_of_manufacture, item.registration_date)
            cursor.execute(create_table, data_for_db)
            connection.commit()
        print(f"Додано рядків: {cursor.rowcount}")
        select_command = '''SELECT * FROM cars_table;'''
        cursor = connection.cursor()
        cursor.execute(select_command)
        cars = cursor.fetchall()
        for car in cars:
            print(car)
        cursor.close()
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()
            print("З'єднання з SQLite закрито")

def search_toyota_2007():
    connection = None
    try:
        select_command = '''SELECT * FROM cars_table WHERE car_brand=? AND registration_date<=?;'''
        connection = sqlite3.connect(file_db)
        cursor = connection.cursor()
        cursor.execute(select_command, ("Toyota", 2007))
        sample_selection = cursor.fetchall()
        for sample in sample_selection:
            print(sample)
        cursor.close()
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()
            print("З'єднання з SQLite закрито")

def main():
    while True:
        print("""
            1 — Створити таблицю
            2 — Вивести відомості про машини марки Тойота, зареєстровані до 2007-го року
            3 — Додати строки до таблиці
            0 — Вийти
            """)

        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            create_db()

        elif choice == "2":
            search_toyota_2007()

        elif choice == "3":
            insert_rows_into_db(list_cars)

        elif choice == "0":
            print("Програму завершено.")
            break

        else:
            print("Невірний пункт меню.")

if __name__ == "__main__":
    main()