from laptop import Laptop

class AppleLaptop(Laptop):
    def __init__(self, brand, screen_size, price, ram, model_name, processor):
        super().__init__(brand, screen_size, price, ram)
        self.__model_name = self.__validate_model_name(model_name)
        self.__processor = self.__validate_processor(processor)

    @property
    def model_name(self):
        return self.__model_name
    @property
    def processor(self):
        return self.__processor

    @model_name.setter
    def model_name(self, value):
        self.__model_name = self.__validate_model_name(value)
    @processor.setter
    def processor(self, value):
        self.__processor = self.__validate_processor(value)

    def __validate_model_name(self, value):
        if not isinstance(value, str):
            raise ValueError("model_name must be a string")
        value = value.strip()
        if not value:
            raise ValueError("model_name cannot be empty")
        return value
    def __validate_processor(self, value):
        if not isinstance(value, str):
            raise ValueError("processor must be a string")
        value = value.strip()
        if not value:
            raise ValueError("processor cannot be empty")
        return value

    def __str__(self):
        return (
            f"AppleLaptop(brand={self.brand}, screen_size={self.screen_size}, "
            f"price={self.price}, ram={self.ram}, model_name={self.model_name}, "
            f"processor={self.processor})"
        )