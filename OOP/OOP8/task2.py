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


def main():
    # завантажити існуючі посилання з txt
    links = load_links()

    # додавання нових посилань
    for i in range(3):
        url = input("Введіть посилання: ")
        short_name = input("Введіть коротку назву: ")
        links[short_name] = url

    # зберегти оновлену базу у txt
    save_links(links)

    # пошук по короткій назві
    name = input("Введіть коротку назву для пошуку: ")
    if name in links:
        print("Посилання:", links[name])
    else:
        print("Такої назви не знайдено")


if __name__ == "__main__":
    main()