# Створіть співпрограму, яка отримує контент із зазначених посилань і логує хід виконання в database, використовуючи стандартну
# бібліотеку requests, а потім проробіть те саме з бібліотекою aiohttp. Кроки, які мають бути залоговані: початок запиту до
# адреси X, відповідь для адреси X отримано зі статусом 200. Перевірте хід виконання програми на >3 ресурсах і перегляньте
# послідовність запису логів в обох варіантах і порівняйте результати. Для двох видів завдань використовуйте різні файли для
# логування, щоби порівняти отриманий результат.

import asyncio
import sqlite3
import time
from datetime import datetime
from pathlib import Path

import requests

db_file = Path(__file__).parent/"http_requests.db"
sequential_log_file = Path(__file__).parent/"sequential.log"
concurrent_log_file = Path(__file__).parent/"concurrent.log"

# Адреси локального HTTP-сервера.
con_urls = ["http://127.0.0.1:8000/", "http://127.0.0.1:8000/", "http://127.0.0.1:8000/",]

def create_database():
    #Створює SQLite-базу даних і таблицю для логів.
    connection = sqlite3.connect(db_file)

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS http_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            mode TEXT NOT NULL,
            message TEXT NOT NULL
        )
        """
    )

    connection.commit()

    return connection

def write_log(connection, log_file, mode, message):
    """
    Записує повідомлення одночасно:
    1. у текстовий файл;
    2. у SQLite-базу даних.
    """
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    log_line = (
        f"{created_at} | "
        f"{mode} | "
        f"{message}\n"
    )

    log_file.write(log_line)
    log_file.flush()

    connection.execute("INSERT INTO http_requests(created_at, mode, message) VALUES (?, ?, ?)",
        (created_at, mode, message,))

    connection.commit()

async def get_content(url, mode, connection, log_file):
    #Асинхронна функція, яка виконує HTTP GET-запит.
    write_log(connection, log_file, mode, f"Початок запиту до адреси {url}")

    try:
        response = await asyncio.to_thread(requests.get, url, timeout=10)

        if response.status_code == 200:
            write_log(connection, log_file, mode,
                (
                    f"Відповідь для адреси {url} "
                    f"отримано зі статусом 200"
                )
            )

            return response.text

        write_log(connection, log_file, mode,
            (
                f"Відповідь для адреси {url} "
                f"отримано зі статусом "
                f"{response.status_code}"
            )
        )

        return None

    except requests.RequestException as error:
        write_log(connection, log_file, mode,
            (
                f"Помилка під час запиту до адреси "
                f"{url}: {error}"
            )
        )

        return None

async def run_sequential(urls, connection):
    #Послідовне виконання HTTP-запитів.
    mode = "sequential"

    started_at = time.perf_counter()

    successful_results = 0

    with sequential_log_file.open("w", encoding="utf-8") as log_file:

        for url in urls:
            content = await get_content(url, mode, connection, log_file)

            if content is not None:
                successful_results += 1

    elapsed = time.perf_counter() - started_at

    print(
        f"Послідовний режим: "
        f"{successful_results}/{len(urls)} успішних запитів, "
        f"{elapsed:.3f} секунд"
    )

    return elapsed


async def run_concurrent(urls, connection):
    #Конкурентне виконання HTTP-запитів.
    mode = "concurrent"

    started_at = time.perf_counter()

    with concurrent_log_file.open("w", encoding="utf-8") as log_file:

        tasks = []

        for url in urls:
            task = asyncio.create_task(get_content(url, mode, connection, log_file))

            tasks.append(task)

        results = await asyncio.gather(*tasks)

    successful_results = sum(content is not None for content in results)

    elapsed = time.perf_counter() - started_at

    print(
        f"Конкурентний режим: "
        f"{successful_results}/{len(urls)} успішних запитів, "
        f"{elapsed:.3f} секунд"
    )

    return elapsed


def show_log_sequence(connection):
    #Виводить послідовність логів із бази даних.
    print("\nПослідовність записів у базі даних:")

    rows = connection.execute("SELECT id, created_at, mode, message FROM http_requests ORDER BY id").fetchall()

    for row_id, created_at, mode, message in rows:
        print(
            f"{row_id:03d} | "
            f"{created_at} | "
            f"{mode:10} | "
            f"{message}"
        )

async def main():
    connection = create_database()

    try:
        sequential_time = await run_sequential(con_urls, connection)
        concurrent_time = await run_concurrent(con_urls, connection)
        print("\nПорівняння часу виконання:")
        print(f"Послідовно:  {sequential_time:.3f} секунд")
        print(f"Конкурентно: {concurrent_time:.3f} секунд")
        show_log_sequence(connection)
    finally:
        connection.close()

if __name__ == "__main__":
    asyncio.run(main())