# Перепишіть домашнє завдання попереднього уроку (сервіс для скорочення посилань) таким чином, щоб у нього була основна частина, яка
# відповідала би за логіку роботи та надавала узагальнений інтерфейс, і модуль представлення, який відповідав би за взаємодію з користувачем.
# При заміні останнього на інший, який взаємодіє з користувачем в інший спосіб, програма має продовжувати коректно працювати.
import os
from pathlib import Path

file_name = Path(__file__).parent/"links.txt"

def load_links():
    links = {}
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # розбиваємо рядок: перше слово — коротка назва, решта — url
                parts = line.split(maxsplit=2)
                if len(parts) >= 2:
                    short_name = parts[0]
                    url = parts[1]
                    links[short_name] = url
    return links


def save_links(links):
    with open(file_name, "w", encoding="utf-8") as f:
        for short_name, url in links.items():
            f.write(f"{short_name} {url}\n")