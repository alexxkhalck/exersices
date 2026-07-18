# Написати функцію, яка за допомогою регулярних виразів розбиває текст на окремі слова і знаходить частоту окремих слів.
import re

some_sring = 'kldjflsk black lskdgfj black skldggmslvlksmr black'

def re_expression():
    count = 0
    frequency = {}
    #list_result = re.findall(r'\w+\s?', some_sring)
    list_result = re.findall(r'\b\w+\b', some_sring)
    for item in list_result:
        frequency[item] = frequency.get(item, 0) + 1

    print(list_result)
    for item, count in frequency.items():
        print(f'Слово "{item}" зустрічається {count} раз(и).')

re_expression()