# Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися
# відгуки до неї.
class Book:
    def __init__(self, author, title, publication, genre):
        self.title = title
        self.author = author
        self.publication = publication
        self.genre = genre
        self.discbook = []

    def __str__(self):
        text = (
            f'Book: {self.title}, Author: {self.author}, '
            f'Publication: {self.publication}, Genre: {self.genre}'
        )
        return text

    def add_disc(self, user_discription):
        self.discbook.append(user_discription)


class Discriptions:
    def __init__(self, member, discbook):
        self.member = member
        self.discbook = discbook

    def __str__(self):
        return f'{self.member}: {self.discbook}'

userlib = [Book(author='J. Martin', title='Song of the ice and flame', publication=2007, genre='fantasy'),
           Book(author='H. Melville', title='Mobidick', publication=1851, genre='A sea adventure'),
           Book(author='F. Herbert', title='Duna', publication=1965, genre='A science fiction'),
           Book(author='A. C. Doyle', title='Sherlock Holmes', publication=1887, genre='Detective'),
           Book(author='A. Dumas', title='The Three Musketeers', publication=1844, genre='An adventure')]

print('В бібліотеці є 5 книг.')
u_counter = 0
for i in userlib:
    u_counter += 1
    print(u_counter, ' - ', i.title)
num = int(input('До якої з них бажаєте залишити відгук?'))

u_disc = Discriptions(input("Ім'я: "), input('Відгук: '))

userlib[num - 1].add_disc(u_disc)

print(userlib[num - 1].title, userlib[num - 1].author, userlib[num - 1].publication, userlib[num - 1].genre)
for disc in userlib[num - 1].discbook:
    print(disc.member, ':', disc.discbook)