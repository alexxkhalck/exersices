# Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву,
# рік видання та жанр. Створіть кілька різних книжок.
# Визначте для нього методи _repr_ та _str_.
class Book:
    def __init__(self,author,title,publication,genre):
            self.title = title
            self.author = author
            self.publication = publication
            self.genre = genre

    def __str__(self):
        return (f'Book: {self.title}, Author: {self.author}, '
                f'Publication: {self.publication}, Genre: {self.genre}')

    def __repr__(self):
        return (f'Book: {self.title}, Author: {self.author}, '
                f'Publication: {self.publication}, Genre: {self.genre}')

iceandflame = Book(author='J. Martin', title='Song of the ice and flame', publication=2007, genre='fantasy')
mobidick = Book(author='H. Melville', title='Mobidick', publication=1851, genre='A sea adventure')
duna = Book(author='F. Herbert', title='Duna', publication=1965, genre='A science fiction')
sherlockholmes = Book(author='A. C. Doyle', title='Sherlock Holmes', publication=1887, genre='Detective')
threemusketeers = Book(author='A. Dumas', title='The Three Musketeers', publication=1844, genre='An adventure')

print(str(iceandflame))
print(repr(iceandflame))