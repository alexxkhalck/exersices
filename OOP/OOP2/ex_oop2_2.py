# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші.
# Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника.
# Викличте метод натискання на кнопку.
class GraphicObject:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


class Rectangle(GraphicObject):
    def __init__(self, x, y, width, height, color='black'):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle at ({self.x}, {self.y}), {self.width}x{self.height}, color={self.color}'


class ClickableObject(GraphicObject):
    def on_click(self):
        print('Об’єкт натиснули мишею.')


class Button(Rectangle, ClickableObject):
    def __init__(self, x, y, width, height, text, color='gray'):
        super().__init__(x, y, width, height, color)
        self.text = text

    def on_click(self):
        print(f'Кнопку "{self.text}" натиснуто.')


button = Button(10, 20, 100, 40, 'OK')
rectangle = Rectangle(5, 5, 80, 30)

print(rectangle)
button.on_click()