# Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл
class UserClass:
    def user_gen_meth(self, some_list):
        g = (i ** 2 for i in some_list)
        return g

    def user_loop_meth(self, some_list):
        res_list = []
        for i in some_list:
            i = i ** 2
            res_list.append(i)
        print(list(res_list))

user_list = [2, 4, 6, 8, 10]

uc = UserClass()
g = uc.user_gen_meth(user_list)
print(list(g))
uc.user_loop_meth(user_list)