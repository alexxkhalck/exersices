# Створіть агрегатні функції для підрахунку загальної кількості  витрат i прибуткiв за місяць.
# Забезпечте відповідний інтерфейс користувача.
import sqlite3
from pathlib import Path

def number_of_expenses():
    db_file = Path(__file__).parent/"materials.db"
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        expenses_table = '''SELECT expense FROM payment_table'''
        cursor = connection.cursor()
        cursor.execute(expenses_table)
        selects_expense = cursor.fetchall()
        expenses = sum(item[0] for item in selects_expense if item[0] is not None)
        print(f"Підрахунок витрат: {expenses}")
        connection.commit()
    except sqlite3.Error as e:
            print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()
            print("З'єднання з SQLite закрито")

def number_of_profits():
    db_file = Path(__file__).parent/"materials.db"
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        revenue_table = '''SELECT revenue FROM payment_table'''
        cursor = connection.cursor()
        cursor.execute(revenue_table)
        selects_revenues = cursor.fetchall()
        revenues = sum(item[0] for item in selects_revenues if item[0] is not None)
        print(f"Підрахунок доходів: {revenues}")
        connection.commit()
    except sqlite3.Error as e:
            print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()
            print("З'єднання з SQLite закрито")

def make_a_new_records():
    db_file = Path(__file__).parent/"materials.db"
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        insert_command = '''INSERT INTO payment_table
                          (purpose, expense, user_time, revenue)
                          VALUES ('Payment', 57.30, datetime('now', 'localtime'), 2.86);'''
        cursor = connection.cursor()
        cursor.execute(insert_command)
        connection.commit()
    except sqlite3.Error as e:
            print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()
            print("З'єднання з SQLite закрито")

def main():
    while True:
        print("""
        1 — Додати платіж
        2 — Показати витрати та прибутки за місяць
        0 — Вийти
        """)

        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            make_a_new_records()
        elif choice == "2":
            number_of_expenses()
            number_of_profits()
        elif choice == "0":
            print("Програму завершено.")
            break
        else:
            print("Невірний пункт меню.")

if __name__ == "__main__":
    main()