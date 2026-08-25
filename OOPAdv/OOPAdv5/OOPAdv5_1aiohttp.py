# Друга частина завдання з модулем aiohttp
import asyncio
import sqlite3
import time
from datetime import datetime
from pathlib import Path

import aiohttp

db_file = Path(__file__).parent/"http_aiohttps.db"
sequential_log_file = Path(__file__).parent/"seq_aiohttp.log"
concurrent_log_file = Path(__file__).parent/"con_aiohttp.log"

# Адреси локального HTTP-сервера.
con_urls = ["http://127.0.0.1:8000/", "http://127.0.0.1:8000/", "http://127.0.0.1:8000/",]

def create_database():
    # Створює SQLite-базу даних та таблицю для зберігання логів.
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

def write_log(connection, log_file,
    mode, message):
    #Записує повідомлення у файл та у SQLite-базу даних.
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    log_line = (
        f"{created_at} | "
        f"{mode} | "
        f"{message}\n"
    )

    # Запис у текстовий файл.
    log_file.write(log_line)
    log_file.flush()

    # Запис у SQLite.
    connection.execute("INSERT INTO http_requests(created_at, mode, message) VALUES (?, ?, ?)", (created_at, mode, message))

    connection.commit()

async def get_content(session, url, mode, connection, log_file):
    #Виконує асинхронний HTTP GET-запит за допомогою aiohttp.
    write_log(connection, log_file, mode, f"Початок запиту до адреси {url}")

    try:
        timeout = aiohttp.ClientTimeout(total=10)

        async with session.get(url, timeout=timeout) as response:

            content = await response.text()

            if response.status == 200:
                write_log(connection, log_file, mode,
                    (
                        f"Відповідь для адреси {url} "
                        f"отримано зі статусом 200"
                    )
                )

                return content

            write_log(connection, log_file, mode,
                (
                    f"Відповідь для адреси {url} "
                    f"отримано зі статусом "
                    f"{response.status}"
                )
            )

            return None

    except (aiohttp.ClientError, asyncio.TimeoutError) as error:
        write_log(connection, log_file, mode,
            (
                f"Помилка під час запиту до адреси "
                f"{url}: {error}"
            )
        )

        return None

async def run_sequential(session, urls, connection):
    #Послідовне виконання запитів.
    mode = "sequential"

    started_at = time.perf_counter()
    successful_requests = 0

    with sequential_log_file.open("w", encoding="utf-8" ) as log_file:

        for url in urls:
            content = await get_content(session, url, mode, connection, log_file)

            if content is not None:
                successful_requests += 1

    elapsed = time.perf_counter() - started_at

    print(
        f"Послідовний режим: "
        f"{successful_requests}/{len(urls)} "
        f"успішних запитів, "
        f"{elapsed:.3f} секунд"
    )

    return elapsed

async def run_concurrent(session, urls, connection):
    #Конкурентне виконання запитів.
    mode = "concurrent"

    started_at = time.perf_counter()

    with concurrent_log_file.open("w", encoding="utf-8") as log_file:

        tasks = []

        for url in urls:
            task = asyncio.create_task(get_content(session, url, mode, connection, log_file))

            tasks.append(task)

        results = await asyncio.gather(*tasks)

    successful_requests = sum(result is not None for result in results)

    elapsed = time.perf_counter() - started_at

    print(
        f"Конкурентний режим: "
        f"{successful_requests}/{len(urls)} "
        f"успішних запитів, "
        f"{elapsed:.3f} секунд"
    )
    return elapsed

def show_log_sequence(connection):
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
        async with aiohttp.ClientSession() as session:
            sequential_time = await run_sequential(session, con_urls, connection)
            concurrent_time = await run_concurrent(session, con_urls, connection)

        print("\nПорівняння часу виконання:")
        print(
            f"Послідовно:  "
            f"{sequential_time:.3f} секунд"
        )
        print(
            f"Конкурентно: "
            f"{concurrent_time:.3f} секунд"
        )

        show_log_sequence(connection)

    finally:
        connection.close()

if __name__ == "__main__":
    asyncio.run(main())