from applelaptop import AppleLaptop
import pickle

def find_laptop_with_max_screen(list_laptops: list[AppleLaptop]) -> AppleLaptop:
    max_screen_laptop = list_laptops[0]

    for laptop in list_laptops:
        if laptop.screen_size > max_screen_laptop.screen_size:
            max_screen_laptop = laptop

    return max_screen_laptop

def find_laptop_with_min_screen(list_laptops: list[AppleLaptop]) -> AppleLaptop:
    min_screen_laptop = list_laptops[0]

    for laptop in list_laptops:
        if laptop.screen_size < min_screen_laptop.screen_size:
            min_screen_laptop = laptop

    return min_screen_laptop

def find_cheapest_laptop(list_laptops: list[AppleLaptop]) -> AppleLaptop:
    cheapest_laptop = list_laptops[0]

    for laptop in list_laptops:
        if laptop.price < cheapest_laptop.price:
            cheapest_laptop = laptop

    return cheapest_laptop

def find_most_expensive_laptop(list_laptops: list[AppleLaptop]) -> AppleLaptop:
    most_expensive_laptop = list_laptops[0]

    for laptop in list_laptops:
        if laptop.price > most_expensive_laptop.price:
            most_expensive_laptop = laptop

    return most_expensive_laptop

def find_laptop_with_max_ram(list_laptops: list[AppleLaptop]) -> AppleLaptop:
    max_ram_laptop = list_laptops[0]

    for laptop in list_laptops:
        if laptop.ram > max_ram_laptop.ram:
            max_ram_laptop = laptop

    return max_ram_laptop

def find_laptop_with_min_ram(list_laptops: list[AppleLaptop]) -> AppleLaptop:
    min_ram_laptop = list_laptops[0]

    for laptop in list_laptops:
        if laptop.ram < min_ram_laptop.ram:
            min_ram_laptop = laptop

    return min_ram_laptop

def save_all_search_results(list_laptops: list[AppleLaptop]) -> None:
    try:
        search_results = [
            find_laptop_with_max_screen(list_laptops),
            find_laptop_with_min_screen(list_laptops),
            find_cheapest_laptop(list_laptops),
            find_most_expensive_laptop(list_laptops),
            find_laptop_with_max_ram(list_laptops),
            find_laptop_with_min_ram(list_laptops)
        ]

        with open("search_results.txt", "wb") as file:
            pickle.dump(search_results, file)

    except Exception as error:
        print(f"Помилка: {error}")

def read_search_results():
    try:
        with open("search_results.txt", "rb") as file:
            return pickle.load(file)

    except Exception as error:
        print(f"Помилка: {error}")

def deserialize_search_results() -> None:
    try:
        laptops = read_search_results()

        iterator = iter(laptops)

        while True:
            try:
                laptop = next(iterator)
                print(laptop)
            except StopIteration:
                break

    except Exception as error:
        print(f"Помилка під час десеріалізації: {error}")