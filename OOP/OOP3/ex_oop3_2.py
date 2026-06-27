# Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting().
# Обидва створюють різні привітання. Створіть два відповідні об'єкти з двох класів вище та викличте дії
# цих двох об'єктів в одній функції (функція hello_friend).
class EngLang:
    @staticmethod
    def greeting(self):
        print('Hello friend! I wish you all the best!')

class SpanLang:
    @staticmethod
    def greeting(self):
        print('¡Hola amigo! ¡Te deseo todo lo mejor!')

def hello_friend(lang1, lang2):
    return lang1.greeting(), lang2.greeting()

eng = EngLang()
span = SpanLang()
hello_friend(eng, span)