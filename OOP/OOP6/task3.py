# Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).
class UserIter:
    class _ReverseIterator:
        def __init__(self, iterable):
            self.__data = list(iterable)
            self.__index = len(self.data) - 1

        @property
        def data(self):
            return self.__data
        @property
        def index(self):
            return self.__index

        @data.setter
        def data(self, data):
            self.__data = data
        @index.setter
        def index(self, index):
            self.__index = index

        def __iter__(self):
            return self

        def __next__(self):
            if self.index < 0:
                raise StopIteration
            value = self.data[self.index]
            self.index -= 1
            return value

    def __init__(self):
        self.__iterable = [10, 20, 30, 40]

    @property
    def iterable(self):
        return self.__iterable

    def user_iterable_loop(self):
        iter_obj = UserIter._ReverseIterator(self.iterable)

        while True:
            try:
                item = next(iter_obj)
                print(item)
            except StopIteration:
                break


ui = UserIter()
ui.user_iterable_loop()