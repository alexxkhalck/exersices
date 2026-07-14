# Назва, частота, обсяг оперативної пам'яті, наявність DVD ROM, вартість,
# Визначити кількість комп'ютерів з об'ємом оперативної пам'яті більше 10 Гбайт і надрукувати всі відомості про них
# name, frequency, amount_of_RAM, presence_of_DVD_ROM, cost
class ShopProduct:
    def __init__(self, name, frequency, amount_of_RAM, presence_of_DVD_ROM, cost):
        self.__name = name
        self.__frequency = frequency
        self.__amount_of_RAM = amount_of_RAM
        self.__presence_of_DVD_ROM = presence_of_DVD_ROM
        self.__cost = cost

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