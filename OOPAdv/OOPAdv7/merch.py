class Merchandice:
    def __init__(self, name: str, cost: float, frequency: int = 1000, amount_of_RAM: int = 8, presence_of_DVD_ROM: bool = False):
        self.__name = self.__validate_name(name)
        self.__cost = self.__validate_cost(cost)
        self.__frequency = self.__validate_frequency(frequency)
        self.__amount_of_RAM = self.__validate_amount_of_RAM(amount_of_RAM)
        self.__presence_of_DVD_ROM = self.__validate_presence_of_DVD_ROM(presence_of_DVD_ROM)

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
        if not isinstance(value, float) or value < 500:
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