# Напишіть декоратор, який буде заміряти час виконання для наданої функції.
import time

def user_decorator(fn):
    def wrapper(*args, **kwargs):
        u_start = time.time()
        result = fn(*args, **kwargs)
        u_end = time.time()
        print(f'Функція виконалась за {u_end - u_start} c.')
        return result
    return wrapper

@user_decorator
def the_func():
    time.sleep(1)

the_func()