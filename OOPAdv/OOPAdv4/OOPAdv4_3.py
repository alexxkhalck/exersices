# Змініть таблицю так, щоби можна було додати не лише витрати, а й прибутки
import sqlite3
from pathlib import Path

def change_db():
    db_file = Path(__file__).parent/"materials.db"
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        rename_table = '''ALTER TABLE payment_table
                            RENAME COLUMN summ TO expense;'''
        change_table = '''ALTER TABLE payment_table
                            ADD COLUMN revenue REAL NOT NULL DEFAULT 0;'''
        cursor = connection.cursor()
        cursor.execute(rename_table)
        connection.commit()
        cursor.execute(change_table)
        connection.commit()
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()
            print("З'єднання з SQLite закрито")

def check_the_record():
    db_file = Path(__file__).parent/"materials.db"
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        check_the_table = '''SELECT * FROM payment_table'''
        cursor = connection.cursor()
        cursor.execute(check_the_table)
        selects = cursor.fetchall()
        for select in selects:
            print(select)
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

#change_db()
#make_a_new_records()
check_the_record()