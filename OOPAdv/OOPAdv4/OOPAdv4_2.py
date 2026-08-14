# Створіть консольний інтерфейс (CLI) на Python для додавання нових записів до бази даних.
import sqlite3
from pathlib import Path

def make_a_new_records():
    db_file = Path(__file__).parent/"materials.db"
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        insert_command = '''INSERT INTO payment_table
                          (purpose, summ, user_time)
                          VALUES ('Payment', 65.34, datetime('now', 'localtime'));'''
        cursor = connection.cursor()
        cursor.execute(insert_command)
        connection.commit()
    except sqlite3.Error as e:
            print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()
            print("З'єднання з SQLite закрито")

def to_be_or_not_to_be():
    flag = True
    print('Якщо ви бажаєте внести нові записи натисніть y, Y або yes')
    print('Якщо ви не бажаєте продовжувати запис натисніть n, N, q або no')
    while flag:
        if input('Make your choise').lower() in ('y', 'yes'):
            make_a_new_records()
        else:
            flag = False

def select_db():
    db_file = Path(__file__).parent/"materials.db"
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        select_command = '''SELECT * FROM payment_table;'''
        cursor = connection.cursor()
        cursor.execute(select_command)
        payments = cursor.fetchall()
        for payment in payments:
            print(payment)
        connection.commit()
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()
            print("З'єднання з SQLite закрито")

to_be_or_not_to_be()
select_db()