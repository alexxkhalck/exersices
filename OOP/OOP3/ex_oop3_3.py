# Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як
# властивості. Ознайомтеся з декоратором property у Python. Створіть клас, що описує температуру і дозволяє
# задавати та отримувати температуру за шкалою Цельсія та Фаренгейта, причому дані можуть бути задані в
# одній шкалі, а отримані в іншій.
class Temperature:
    def __init__(self):
        self.__temperature = None
        self.__meas_system = None

    @property
    def temperature(self):
        return self.__temperature
    @property
    def meas_system(self):
        return self.__meas_system

    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature
    @meas_system.setter
    def meas_system(self, meas_system):
        self.__meas_system = meas_system

    @staticmethod
    def measurement(temperature, meas_system):
        match meas_system:
            case 'C':
                # Цельсій = (Фаренгейт (°C) - 32) / 1,8
                celsius = (temperature - 32) / 1.8
                return celsius
            case 'F':
                # Фаренгейт = Цельсій (°C)*1,8 + 32
                fahrenheit = (temperature * 1.8) + 32
                return fahrenheit
            case _:
                return 'Ця вимірювальна система не описана'

temp = Temperature()
print(temp.measurement(100, 'F'), 'градусів Цельсія')
print(temp.measurement(30, 'C'), 'градусів Фаренгейта')