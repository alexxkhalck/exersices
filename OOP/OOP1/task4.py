# Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список автомобілів,
# доступних для продажу, і функцію продажу заданого автомобіля.
class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price


class Diller:
    def __init__(self, cars):
        self.cars = cars

    def selling(self):
        buyflag = True

        print('У діллера є такі автомобілі.')
        for i in self.cars:
            print(i.model)

        while buyflag:
            item = input('Який з них бажаєте придбати?')
            car = self.buying(item)
            if car is not None:
                print(f'Ви придбали нову машину {car.model}.')
                buyflag = False
                self.cars.remove(car)
                print(f'Машини які лишилися у диллера')
                for i in self.cars:
                    print(f'{i.model}, {i.price}')
            else:
                print('Бажаєте продовжити вибір?')
                if input().lower() in ('q', 'n'):
                    buyflag = False

    def buying(self, item):
        for i in self.cars:
            if item == str(i.model):
                return i
        print('Диллер не має машини яку ви бажаєте')
        return None


cars = [Car('Ferrary', 1200000), Car('BMW', 200000), Car('Mercedes', 150000)]
diller = Diller(cars)
diller.selling()