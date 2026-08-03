# Створіть функцію-генератор чисел Фібоначчі. Застосуйте до неї декоратор, який залишатиме в послідовності лише парні числа.
# def user_decorator():
#     def gen_fib(n):
#         if n <= 0:
#             return []
#         if n == 1:
#             return [0]
#         res_list = []
#         list_fib = [0, 1]
#         list(map(lambda _: list_fib.append(list_fib[-1] + list_fib[-2]), range(n - 2)))
#         res_list.append([item for item in list_fib if item % 2 == 0])
#         yield res_list
#     return gen_fib

# some_dec = user_decorator()
# result = some_dec(10)

# for item in result:
#     print(item)
def user_decorator(fn):
    def wrapper(n):
        for num in fn(n):
            if num % 2 == 0:
                yield num

    return wrapper


@user_decorator
def gen_fib(n):
    x, y = 0, 1

    for _ in range(n):
        yield x
        x, y = y, x + y


for item in gen_fib(10):
    print(item)