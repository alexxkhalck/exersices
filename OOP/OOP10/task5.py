# З клавіатури вводиться рядок, в якому є інформація про прізвище, ім'я, дату народження, електронну адресу та відгук про курси учня.
# Написати функцію, яка, використовуючи регулярні вирази, витягне дані з рядка і поверне словник.
import re

def parse_student_info(text):
    pattern = r'^(\S+)\s+(\S+)\s+(\d{2}[./-]\d{2}[./-]\d{4})\s+([\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,})\s+(.+)$'
    match = re.match(pattern, text)

    if match:
        return {
            'surname': match.group(1),
            'name': match.group(2),
            'birth_date': match.group(3),
            'email': match.group(4),
            'review': match.group(5)
        }
    return None


text = input("Введіть дані: ")
print(parse_student_info(text))