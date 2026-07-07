# Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).
class UserGen:
    def user_reverse(self, some_list):
        for item in range(len(some_list) - 1, -1, -1):
            yield some_list[item]

input_list = [10, 20, 30, 40, 50, 60, 70]
ug = UserGen()
g = ug.user_reverse(input_list)
for i in g:
    print(i)