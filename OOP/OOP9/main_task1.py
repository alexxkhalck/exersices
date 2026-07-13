from task1 import *

def main():
    # завантажити існуючі посилання з txt
    links = load_links()

    # додавання нових посилань
    for i in range(3):
        url = input("Введіть посилання: ")
        short_name = input("Введіть коротку назву: ")
        links[short_name] = url

    # зберегти оновлену базу у txt
    save_links(links)

    # пошук по короткій назві
    name = input("Введіть коротку назву для пошуку: ")
    if name in links:
        print("Посилання:", links[name])
    else:
        print("Такої назви не знайдено")


if __name__ == "__main__":
    main()