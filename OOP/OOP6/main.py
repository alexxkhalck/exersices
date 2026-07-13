# Виконавець
# Жанр
# Назва
# альбому
# Тираж
#
# Вивести дані про платівки, тираж яких перевищує 10000 примірників.
class UserDisk:
    def __init__(self, artist, genre, album, title, circulation):
        self.__artist = artist
        self.__genre = genre
        self.__album = album
        self.__title = title
        self.__circulation = circulation

    @property
    def artist(self):
        return self.__artist
    @property
    def genre(self):
        return self.__genre
    @property
    def album(self):
        return self.__album
    @property
    def title(self):
        return self.__title
    @property
    def circulation(self):
        return self.__circulation

    @artist.setter
    def artist(self, artist):
        self.__artist = artist
    @genre.setter
    def genre(self, genre):
        self.__genre = genre
    @album.setter
    def album(self, album):
        self.__album = album
    @title.setter
    def title(self, title):
        self.__title = title
    @circulation.setter
    def circulation(self, circulation):
        self.__circulation = circulation

    def __str__(self):
        return f'Artist {self.artist} - Genre {self.genre} - Album {self.album} - Title {self.title} - Circulation {self.circulation}'

    @staticmethod
    def printing_in_console(obj):
        print(f'Artist {obj.artist} - Genre {obj.genre} - Album {obj.album} - Title {obj.title} - Circulation {obj.circulation}')

class SomeClass:
    def __init__(self):
        pass

    @classmethod
    def printing(self, some_list):
        for disk in some_list:
            if disk.circulation > 10000:
                disk.printing_in_console(disk)

udspring = UserDisk("Arthur", "Jaz", "Sun", "Spring", 20000)
udsubmarine = UserDisk("Beetles", "Rock", "Submarine", "Submarine", 200000)
udunforgiven = UserDisk("Metallica", "Rock", "Unforgiven", "Unforgiven", 2000)
udyiiii = UserDisk("McMat", "Country", "Yiiii Haaaa", "Yiiii Haaaa", 9000)
udsome = UserDisk("Gaga", "Pop", "Some", "Some thing", 15000)
udwinter = UserDisk("Arthur", "Jaz", "Sun", "Winter", 1000)

list_of_the_disks = [udspring, udsubmarine, udunforgiven, udyiiii, udsome, udwinter]

# printing(list_of_the_disks)
sc = SomeClass()
sc.printing(list_of_the_disks)