# Створіть функцію для обчислення факторіала числа. Запустіть декілька завдань, використовуючи Thread, і заміряйте
# швидкість їхнього виконання, а потім заміряйте швидкість обчислення, використовуючи той же набір завдань на
# ThreadPoolExecutor. Як приклади використовуйте останні значення, від мінімальних і до максимально можливих,
# щоб побачити приріст або втрату продуктивності.
from functools import reduce
import time
import threading
from concurrent.futures import ThreadPoolExecutor

def user_decorator(fn):
    def wrapper(n):
        start_time = time.time()
        res = fn(n)
        end_time = time.time()
        print(f"Функція виконувалася {end_time - start_time} c. і має результат {res}")
        return res
    return wrapper

@user_decorator
def fact(n):
    if n < 0:
        raise ValueError("Не вірний формат ")
    res = reduce(lambda x, y: x * y, range(1, n + 1))
    return res

def main():
    first_factorial = threading.Thread(target=fact, args=(5,))
    second_factorial = threading.Thread(target=fact, args=(5,))

    first_start_time = time.time()
    first_factorial.start()
    first_factorial.join()
    first_end_time = time.time()

    second_start_time = time.time()
    second_factorial.start()
    second_factorial.join()
    second_end_time = time.time()

    print('Перша частина завдання')
    print(f"Перший потік виконувався {first_end_time - first_start_time} c.")
    print(f"Другий потік виконувався {second_end_time - second_start_time} c.")

    with ThreadPoolExecutor(max_workers=2) as exec:
        future1 = exec.submit(fact, 5)
        future2 = exec.submit(fact, 5)

        start_time_TPE1 = time.time()
        res1 = future1.result()
        end_time_TPE1 = time.time()

        start_time_TPE2 = time.time()
        res2 = future2.result()
        end_time_TPE2 = time.time()

        print('Друга частина завдання')
        print(f"Перший потік ThreadPoolExecutor виконувався {end_time_TPE1 - start_time_TPE1} c. результат першого потоку {res1}")
        print(f"Другий потік ThreadPoolExecutor виконувався {end_time_TPE2 - start_time_TPE2} c. результат першого потоку {res2}")

if __name__ == "__main__":
    main()