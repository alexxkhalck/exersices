# За допомогою написаного Вами декоратору заміряйте та порівняйте швидкість роботи цих 4х варіантів.
import functools
import time

def fib_func(n):
    start_time = time.time()
    if n <= 0:
        return []
    if n == 1:
        return [0]
    return_list = [0, 1]
    list(map(lambda _: return_list.append(return_list[-1] + return_list[-2]), range(n - 2)))
    end_time = time.time()
    print(f'Виконання функції без кешу зайняло {end_time - start_time} c.')
    return return_list

@functools.lru_cache()
def fib_func_lru_max(n):
    start_time = time.time()
    if n <= 0:
        return []
    if n == 1:
        return [0]
    return_list = [0, 1]
    list(map(lambda _: return_list.append(return_list[-1] + return_list[-2]), range(n - 2)))
    end_time = time.time()
    print(f'Виконання функції з максимальним кешом зайняло {end_time - start_time} c.')
    return return_list

@functools.lru_cache(maxsize=10)
def fib_func_lru_10(n):
    start_time = time.time()
    if n <= 0:
        return []
    if n == 1:
        return [0]
    return_list = [0, 1]
    list(map(lambda _: return_list.append(return_list[-1] + return_list[-2]), range(n - 2)))
    end_time = time.time()
    print(f'Виконання функції з кешом 10 зайняло {end_time - start_time} c.')
    return return_list

@functools.lru_cache(maxsize=16)
def fib_func_lru_16(n):
    start_time = time.time()
    if n <= 0:
        return []
    if n == 1:
        return [0]
    return_list = [0, 1]
    list(map(lambda _: return_list.append(return_list[-1] + return_list[-2]), range(n - 2)))
    end_time = time.time()
    print(f'Виконання функції з кешом 16 зайняло {end_time - start_time} c.')
    return return_list

fib_list = fib_func(25)

# for i in fib_list:
#     print(f'{i}', end=' ')

print()
fib_list = fib_func_lru_max(25)

# for i in fib_list:
#     print(f'{i}', end=' ')
print()
fib_list = fib_func_lru_10(25)

# for i in fib_list:
#     print(f'{i}', end=' ')
print()
fib_list = fib_func_lru_16(25)

# for i in fib_list:
#     print(f'{i}', end=' ')