# Створіть функцію, яка приймає список з елементів типу int, а повертає новий список з рядкових значень вихідного масиву.
# Додайте анотацію типів для вхідних і вислідних значень функції.
def transformation(some_list: list[int])->list[str]:
    return list(map(str, some_list))

user_list = [12, 13, 14, 15]

result = transformation(user_list)

for item in result:
    print(type(item))
    print(item)