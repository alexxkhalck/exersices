# Створіть базу даних обмінних курсів до USD за допомогою API Monobank (api.monobank.ua). Зробіть запити через бібліотеку
# запитів, проаналізуйте результати, запишіть їх у базу даних. (Потрібно 3 приклади)
import sqlite3
from pathlib import Path
from datetime import datetime

import requests

API_URL = "https://api.monobank.ua/bank/currency"

DB_FILE = Path(__file__).parent / "currency_rates.db"

UAH = 980
USD = 840
EUR = 978
PLN = 985

CURRENCIES = {
    USD: "USD",
    EUR: "EUR",
    PLN: "PLN"
}

def create_database():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS currency_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_code INTEGER NOT NULL,
            currency_name TEXT NOT NULL,
            base_currency_code INTEGER NOT NULL,
            rate_buy REAL,
            rate_sell REAL,
            rate_cross REAL,
            api_date TEXT NOT NULL,
            loaded_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

def get_currency_rates():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print(f"Помилка запиту до Monobank API: {error}")
        return []

def select_needed_rates(api_data):
    selected_rates = []

    for item in api_data:
        currency_a = item["currencyCodeA"]
        currency_b = item["currencyCodeB"]

        # Залишаємо USD/UAH, EUR/UAH, PLN/UAH
        if currency_a in CURRENCIES and currency_b == UAH:
            selected_rates.append(item)

    return selected_rates

def save_rates_to_database(rates):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    loaded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for rate in rates:
        currency_code = rate["currencyCodeA"]

        api_date = datetime.fromtimestamp(
            rate["date"]
        ).strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            INSERT INTO currency_rates (
                currency_code,
                currency_name,
                base_currency_code,
                rate_buy,
                rate_sell,
                rate_cross,
                api_date,
                loaded_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            currency_code,
            CURRENCIES[currency_code],
            rate["currencyCodeB"],
            rate.get("rateBuy"),
            rate.get("rateSell"),
            rate.get("rateCross"),
            api_date,
            loaded_at
        ))

    connection.commit()
    connection.close()

def show_analysis(rates):
    if not rates:
        print("Дані про курси не знайдено.")
        return

    print("\nКурси валют Monobank:")

    for rate in rates:
        name = CURRENCIES[rate["currencyCodeA"]]

        buy = rate.get("rateBuy")
        sell = rate.get("rateSell")
        cross = rate.get("rateCross")

        print(f"\n{name}/UAH")

        if buy is not None:
            print(f"Купівля: {buy}")

        if sell is not None:
            print(f"Продаж: {sell}")

        if cross is not None:
            print(f"Крос-курс: {cross}")

        if buy is not None and sell is not None:
            difference = round(sell - buy, 4)
            print(f"Спред: {difference}")

def show_saved_rates():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            currency_name,
            rate_buy,
            rate_sell,
            rate_cross,
            api_date,
            loaded_at
        FROM currency_rates
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    print("\nДані з бази:")

    for row in rows:
        print(row)

    connection.close()

def main():
    create_database()

    api_data = get_currency_rates()
    needed_rates = select_needed_rates(api_data)

    show_analysis(needed_rates)
    save_rates_to_database(needed_rates)

    print("\nКурси успішно записано у currency_rates.db")

    show_saved_rates()

if __name__ == "__main__":
    main()