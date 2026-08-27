# Створіть два класи Directory (тека) і File (файл) з типами (анотацією).
# Клас Directory має мати такі поля:
# ·        назва (name типу str);
# ·        батьківська тека (root типу Directory);
# ·        список файлів (список типу files, який складається з екземплярів File);
# ·        список підтек (список типу sub_directories, який складається з екземплярів Directory).

# Клас Directory має мати такі поля:
# ·        додавання теки до списку підтек (add_sub_directory, який приймає екземпляр Directory та присвоює поле root для приймального екземпляра);
# ·        видалення теки зі списку підтек (remove_sub_directory, який приймає екземпляр Directory та обнуляє поле root. Метод також видаляє теку зі списку sub_directories);
# ·        додавання файлу в теку (add_file, який приймає екземпляр File і присвоює йому поле directory – див. клас File нижче);
# ·        видалення файлу з теки (remove_file, який приймає екземпляр File та обнуляє у нього поле directory. Метод видаляє файл зі списку files).

# Клас File має мати такі поля:
# ·        назва (name типу str);
# ·        тека (Directory типу Directory).
from pathlib import Path

class Directory:
    def __init__(self, name: str, root: Directory|None = None):# , files: list[File], sub_directories: Directory
        self.name: str = name
        self.root: Directory | None = root
        self.files: list[File] = []
        self.sub_directories: list[Directory] = []

    def add_sub_directory(self, directory: Directory):
        directory.root = self
        self.sub_directories.append(directory)

    def remove_sub_directory(self, directory: Directory):
        directory.root = None
        if directory in self.sub_directories:
            self.sub_directories.remove(directory)

    def add_file(self, file: File):
        file.directory = self
        self.files.append(file)

    def remove_file(self, file: File):
        file.directory = None
        if file in self.files:
            self.files.remove(file)

class File:
    def __init__(self, name: str, directory: Directory|None = None):
        self.name: str = name
        self.directory: Directory | None = directory

user_file = Path(__file__).parent/"file.txt"

root = Directory("root")
sub = Directory("sub")
file1 = File(user_file)

root.add_sub_directory(sub)
root.add_file(file1)

print(sub.root.name)          # root
print(file1.directory.name)  # root

root2 = Directory("root2")
root.remove_sub_directory(sub)
root.remove_file(file1)

print(sub.root)        # None
print(file1.directory) # None