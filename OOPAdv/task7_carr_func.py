# Створіть звичайну функцію множення двох чисел. Створіть карированну функцію множення двох чисел.
# Частково застосуйте її до одного аргументу, до двох аргументiв.
def user_mul(x, y):
    return x * y

def user_car_mul_func(x):
    def do_mul(y):
        return x * y
    return do_mul

print('Звичайна функція')
print(user_mul(3,4))

print('Каррована функція')
first_part = user_car_mul_func(3)
print(first_part(4))

print('Каррована функція на два аргумента')
print(user_car_mul_func(3)(4))