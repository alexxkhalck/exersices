# Зробіть таблицю для підрахунку особистих витрат із такими полями: id, призначення, сума, час.
# id, purpose, summ, user_time
import sqlite3
from pathlib import Path

def creating_db_and_table():
    db_file = Path(__file__).parent/"materials.db"
    connection = None
    try:
        connection = sqlite3.connect(db_file)

        db_table = '''CREATE TABLE IF NOT EXISTS payment_table(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        purpose TEXT NOT NULL,
                        summ REAL NOT NULL,
                        user_time datetime);'''
        cursor = connection.cursor()
        cursor.execute(db_table)
        connection.commit()
        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name = 'payment_table'
        """)

        table = cursor.fetchone()

        if table:
            print("Таблиця payment_table існує.")
        else:
            print("Таблицю payment_table не знайдено.")
        cursor.close()
        print("База даних створена.")
    except sqlite3.Error as e:
        print("Помилка при підключенні до sqlite", e)
    finally:
        if connection:
            connection.close()
            print("З'єднання з SQLite закрито")

creating_db_and_table()