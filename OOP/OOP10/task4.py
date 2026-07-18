# Напишіть функцію, яка буде аналізувати текст, що надходить до неї, і виводити тільки унікальні слова на екран,
# загальну кількість слів і кількість унікальних слів.
import re

def analyze_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = sorted(set(words))

    print("Унікальні слова:")
    print(*unique_words)

    print(f"Загальна кількість слів: {len(words)}")
    print(f"Кількість унікальних слів: {len(unique_words)}")

text = input("Введіть текст: ")
analyze_text(text)