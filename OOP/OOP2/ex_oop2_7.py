# Створіть ієрархію класів транспортних засобів. У загальному класі опишіть загальні всім транспортних
# засобів поля, у спадкоємцях – специфічні їм. Створіть кілька екземплярів.
# Виведіть інформацію щодо кожного транспортного засобу.
class AbstractCar:
    def __init__(self, numofwheels, engine, passangers):
        self.numofwheels = numofwheels
        self.engine = engine
        self.passangers = passangers

    def printcar(self):
        print('Машина мае колеса, двигун і може перевозити пасажирів.')

class PersonalCar(AbstractCar):

    def printcar(self):
        super().printcar()
        print(f'Особиста машина має: {self.numofwheels}, двигун потужністю {self.engine} Ватт і перевозе {self.passangers}')

class Bus(AbstractCar):

    def printcar(self):
        super().printcar()
        print(f'Автобус має: {self.numofwheels}, двигун потужністю {self.engine} Ватт і перевозе {self.passangers}')

class Truck(AbstractCar):
    
    def printcar(self):
        super().printcar()
        print(f'Великовантажівка має: {self.numofwheels}, двигун потужністю {self.engine} Ватт і перевозе {self.passangers}')

pcar = PersonalCar(4, 250, 4)
pcar.printcar()

bus = Bus(4, 2500, 40)
bus.printcar()

truck = Truck(6, 2500, 2)
truck.printcar()