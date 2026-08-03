# Напишіть програму яка буде виводити 25 перших чисел Фібоначі, використовуючи для цього три наведені в тексті заняття функції — без кешу,
# з кешем довільної довжини, з кешем з модулю functools з максимальною кількістю 10 елементів та з кешем з модулю functools з максимальною
# кількістю 16 елементів.
import functools
import time

def fib_func(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    return_list = [0, 1]
    list(map(lambda _: return_list.append(return_list[-1] + return_list[-2]), range(n - 2)))
    return return_list

@functools.lru_cache()
def fib_func_lru_max(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    return_list = [0, 1]
    list(map(lambda _: return_list.append(return_list[-1] + return_list[-2]), range(n - 2)))
    return return_list

@functools.lru_cache(maxsize=10)
def fib_func_lru_10(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    return_list = [0, 1]
    list(map(lambda _: return_list.append(return_list[-1] + return_list[-2]), range(n - 2)))
    return return_list

@functools.lru_cache(maxsize=16)
def fib_func_lru_16(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    return_list = [0, 1]
    list(map(lambda _: return_list.append(return_list[-1] + return_list[-2]), range(n - 2)))
    return return_list

fib_list = fib_func(25)

for i in fib_list:
    print(f'{i}', end=' ')

print()
fib_list = fib_func_lru_max(25)

for i in fib_list:
    print(f'{i}', end=' ')
print()
fib_list = fib_func_lru_10(25)

for i in fib_list:
    print(f'{i}', end=' ')
print()
fib_list = fib_func_lru_16(25)

for i in fib_list:
    print(f'{i}', end=' ')