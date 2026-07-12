# Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел. Створіть ще
# один скрипт, який читає числа з файлу та виводить на екран їхню суму.
from pathlib import Path
import random

file_name = Path(__file__).parent/"numbers.txt"

def write_random_numbers(filename, count=10000):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for _ in range(count):
                number = random.random()  # випадкове дійсне число від 0.0 до 1.0
                f.write(f"{number}\n")
    except IOError:
        print('Помилка запису!!!')

if __name__ == "__main__":
    write_random_numbers(file_name)# "C:\\Users\\khalt\\Documents\\JS\\pyCat\\CBS\\OOP\\OOP8\\numbers.txt"
    print("Файл numbers.txt створено і заповнено 10000 випадковими числами.")

def sum_numbers_from_file(filename):
    try:
        total = 0.0
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:  # пропустити порожні рядки, якщо будуть
                    total += float(line)
        return total
    except IOError:
        print('Помилка читання!!!')

if __name__ == "__main__":
    total_sum = sum_numbers_from_file(file_name)
    print(f"Сума чисел з файлу {file_name}: {total_sum}")