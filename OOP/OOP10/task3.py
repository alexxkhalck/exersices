# Користувач вводить з клавіатури пропозицію. Написати функцію, яка друкуватиме на екран останні 3 символи кожного слова.
import re

def print_last_3_chars():
    user_string = input("Введіть речення: ")
    splited_string = re.findall(r'\b\w+\b', user_string)
    result = [str[-3:] for str in splited_string]
    print(*result)

print_last_3_chars()