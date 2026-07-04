# Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable
class UserIter:
    def __init__(self):
        self.__iterable = range(10)

    @property
    def iterable(self):
        return self.__iterable

    def user_iterable_loop(self):
        iter_obj = iter(self.iterable)

        while True:
            try:
                item = next(iter_obj)
                print(item)
            except StopIteration:
                break


ui = UserIter()
ui.user_iterable_loop()