# Створіть три функції, одна з яких читає файл на диску із заданим ім'ям та перевіряє наявність рядка «Wow!». Якщо файлу немає, то
# засипає на 5 секунд, а потім знову продовжує пошук по файлу. Якщо файл є, то відкриває його і шукає рядок «Wow!». За наявності
# цього рядка закриває файл і генерує подію, а інша функція чекає на цю подію і у разі її виникнення виконує видалення цього файлу.
# Якщо рядки «Wow!» не було знайдено у файлі, то засипати на 5 секунд. Створіть файл руками та перевірте виконання програми.
import threading
import time
import os
from pathlib import Path

def check_file(filename, event):
    while not event.is_set():
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            print("Файл не знайдено, сплю 5 секунд...")
            time.sleep(5)
            continue

        if "Wow!" in content:
            print("Рядок 'Wow!' знайдено!")
            event.set()  # генеруємо подію
            return
        else:
            print("Рядка 'Wow!' немає, сплю 5 секунд...")
            time.sleep(5)


def delete_file(filename, event):
    print("Чекаю на подію...")
    event.wait()  # блокується, доки подія не буде встановлена
    try:
        os.remove(filename)
        print(f"Файл '{filename}' видалено!")
    except FileNotFoundError:
        print(f"Файл '{filename}' вже не існує.")

def main():
    filename = Path(__file__).parent/"test.txt"
    event = threading.Event()

    checker = threading.Thread(target=check_file, args=(filename, event))
    deleter = threading.Thread(target=delete_file, args=(filename, event))

    checker.start()
    deleter.start()

    checker.join()
    deleter.join()

    print("Програма завершена.")

if __name__ == "__main__":
    main()