# Створіть список цілих чисел. Отримайте список квадратів непарних чисел із цього списку.
user_list = [2, 3, 4, 5, 6, 7, 8, 9]

user_lambda = filter(lambda x: x%2!=0, user_list)
res_list = list(map(lambda x: x ** 2, user_lambda))

for i in res_list:
    print(i)