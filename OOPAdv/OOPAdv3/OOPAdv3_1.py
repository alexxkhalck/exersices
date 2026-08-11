# Створіть прості словники та конвертуйте їх у JSON. Збережіть JSON у файлі та спробуйте завантажити дані з файлу.
import json
from pathlib import Path

file_json = Path(__file__).parent/"json_task3_1.json"

dict1 = {"name": "Ivan", "lastname": "Ivanov"}
dict2 = {"name": "Petro", "lastname": "Petrov"}
dict3 = {"name": "Sam", "lastname": "Samov"}

dicts = [dict1, dict2, dict3]

def save_file():
    try:
        with open(file_json, "w", encoding="utf-8") as f:
            json.dump(dicts, f, ensure_ascii=False, indent=4)
    except IOError:
        print('I can not create a file.')

def load_from_file():
    try:
        with open(file_json, "r", encoding="utf-8") as f:
            obj = json.load(f)
            return obj
    except FileNotFoundError:
        print("Файл не знайдено")
        return []
    except json.JSONDecodeError:
        print("У файлі некоректний JSON")
        return []

save_file()
obj = load_from_file()
for item in obj:
    print(item)