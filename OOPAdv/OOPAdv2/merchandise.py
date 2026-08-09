# Назва, частота, обсяг оперативної пам'яті, наявність DVD ROM, вартість,
# Обчислити середню вартість усіх комп'ютерів  і надрукувати найменування комп'ютерів та їхню середню вартість
class Merchandice:
    def __init__(self, name, frequency, amount_of_RAM, presence_of_DVD_ROM, cost):
        self.__name = self.__validate_name(name)
        self.__frequency = self.__validate_frequency(frequency)
        self.__amount_of_RAM = self.__validate_amount_of_RAM(amount_of_RAM)
        self.__presence_of_DVD_ROM = self.__validate_presence_of_DVD_ROM(presence_of_DVD_ROM)
        self.__cost = self.__validate_cost(cost)

    def __validate_name(self, value):
        if not isinstance(value, str) or len(value) < 2:
            raise ValueError("Is not correct VALUE")
        return value
    def __validate_frequency(self, value):
        if not isinstance(value, int) or value < 1000:
            raise ValueError("Is not correct VALUE. The frequency too low")
        return value
    def __validate_amount_of_RAM(self, value):
        if not isinstance(value, int) or value < 8:
            raise ValueError("This is not modern PC")
        return value
    def __validate_presence_of_DVD_ROM(self, value):
        if not isinstance(value, bool):
            raise ValueError("Can't be this VALUE")
        return value
    def __validate_cost(self, value):
        if not isinstance(value, int) or value < 500:
            raise ValueError("Is not correct VALUE or very low price")
        return value

    @property
    def name(self):
        return self.__name
    @property
    def frequency(self):
        return self.__frequency
    @property
    def amount_of_RAM(self):
        return self.__amount_of_RAM
    @property
    def presence_of_DVD_ROM(self):
        return self.__presence_of_DVD_ROM
    @property
    def cost(self):
        return self.__cost

    @name.setter
    def name(self, name):
        self.__name = name
    @frequency.setter
    def frequency(self, frequency):
        self.__frequency = frequency
    @amount_of_RAM.setter
    def amount_of_RAM(self, amount_of_RAM):
        self.__amount_of_RAM = amount_of_RAM
    @presence_of_DVD_ROM.setter
    def presence_of_DVD_ROM(self, presence_of_DVD_ROM):
        self.__presence_of_DVD_ROM = presence_of_DVD_ROM
    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    def __str__(self):
        return (f"Name: {self.name}, Frequency: {self.frequency}, "
                f"Amount of RAM: {self.amount_of_RAM}, "
                f"Presence of DVD-ROM: {self.presence_of_DVD_ROM}, "
                f"Cost: {self.cost}")

product1 = Merchandice("Office PC", 3200, 8, True, 15000)
product2 = Merchandice("Gaming PC", 4800, 16, False, 35000)
product3 = Merchandice("Home PC", 2600, 12, True, 12000)
product4 = Merchandice("Mini PC", 2200, 8, False, 18000)
product5 = Merchandice("Workstation", 5200, 32, False, 60000)
product6 = Merchandice("Workstation", 4200, 32, False, 50000)

merch_list = [product1, product2, product3, product4, product5, product6]