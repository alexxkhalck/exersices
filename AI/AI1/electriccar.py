from vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self, brand, year, price, horsepower, batterycapacity, rangekm):
        super().__init__(brand, year, price, horsepower)
        self.__batterycapacity = self.__validate_batterycapacity(batterycapacity)
        self.__rangekm = self.__validate_rangekm(rangekm)

    @property
    def batterycapacity(self):
        return self.__batterycapacity
    @property
    def rangekm(self):
        return self.__rangekm

    @batterycapacity.setter
    def batterycapacity(self, value):
        self.__batterycapacity = self.__validate_batterycapacity(value)
    @rangekm.setter
    def rangekm(self, value):
        self.__rangekm = self.__validate_rangekm(value)

    def __validate_batterycapacity(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("batterycapacity must be a number (kWh)")
        if value <= 0:
            raise ValueError("batterycapacity must be greater than 0")
        return float(value)
    def __validate_rangekm(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("rangekm must be a number (km)")
        if value <= 0:
            raise ValueError("rangekm must be greater than 0")
        return float(value)

    def __str__(self):
        return (
            f"ElectricCar(brand={self.brand}, year={self.year}, price={self.price}, "
            f"horsepower={self.horsepower}, batterycapacity={self.batterycapacity}, rangekm={self.rangekm})"
        )