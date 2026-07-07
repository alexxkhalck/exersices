# Напишіть функцію-генератор для отримання n перших простих чисел.
class SimpleNums:

    def counting(self, num):
        if num < 2:
            return False
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                return False
        return True

    def first_n_nums(self, n):
        count = 0
        num = 2

        while count < n:
            if self.counting(num):
                yield num
                count += 1
            num += 1


sn = SimpleNums()
g = sn.first_n_nums(7)
print(list(g))