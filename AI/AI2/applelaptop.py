from laptop import Laptop

class AppleLaptop(Laptop):
    def __init__(self, brand, screen_size, price, ram,
                 model_name, processor):

        super().__init__(brand, screen_size, price, ram)

        self.__validate_model_name(model_name)
        self.__validate_processor(processor)

    # ---------- Приватні валідатори ----------

    def __validate_model_name(self, model_name):
        if not isinstance(model_name, str):
            raise TypeError("Назва моделі повинна бути рядком.")
        if not model_name.strip():
            raise ValueError("Назва моделі не може бути порожньою.")

        self.__model_name = model_name
    def __validate_processor(self, processor):
        if not isinstance(processor, str):
            raise TypeError("Процесор повинен бути рядком.")
        if not processor.strip():
            raise ValueError("Процесор не може бути порожнім.")

        self.__processor = processor

    # ---------- Властивості ----------

    @property
    def model_name(self):
        return self.__model_name
    @model_name.setter
    def model_name(self, value):
        self.__validate_model_name(value)

    @property
    def processor(self):
        return self.__processor
    @processor.setter
    def processor(self, value):
        self.__validate_processor(value)

    # ---------- Рядкове представлення ----------

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"model_name='{self.__model_name}', "
            f"processor='{self.__processor}'"
        )

macbook = AppleLaptop(
    "Apple",
    14.2,
    2499,
    32,
    "MacBook Pro",
    "Apple M4 Pro"
)

print(macbook)