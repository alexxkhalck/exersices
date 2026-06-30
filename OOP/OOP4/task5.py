# Створіть програму спортивного комплексу, у якій передбачене меню: 1 - перелік видів спорту, 2 - команда
# тренерів, 3 - розклад тренувань, 4 - вартість тренування. Дані зберігати у словниках. Також передбачити
# пошук по прізвищу тренера, яке вводиться з клавіатури у відповідному пункті меню. Якщо ключ не буде
# знайдений, створити відповідний клас-Exception, який буде викликатися в обробнику виключень.
class CoachNotFoundError(Exception):
    pass

sport_types = {
    1: "Футбол",
    2: "Баскетбол",
    3: "Плавання",
    4: "Легка атлетика"
}

trainers = {
    "Іваненко": "Іван Петренко",
    "Шевченко": "Олена Коваль",
    "Кравчук": "Андрій Мельник"
}

schedule = {
    "Футбол": "Пн, Ср, Пт 18:00",
    "Баскетбол": "Вт, Чт 17:30",
    "Плавання": "Пн, Чт 16:00",
    "Легка атлетика": "Сб 10:00"
}

prices = {
    "Футбол": 500,
    "Баскетбол": 450,
    "Плавання": 600,
    "Легка атлетика": 400
}


def find_coach(surname):
    if surname not in trainers:
        raise CoachNotFoundError(f"Тренера з прізвищем '{surname}' не знайдено.")
    return trainers[surname]


while True:
    print("\nМеню:")
    print("1 - перелік видів спорту")
    print("2 - команда тренерів")
    print("3 - розклад тренувань")
    print("4 - вартість тренування")
    print("5 - пошук тренера за прізвищем")
    print("0 - вихід")

    choice = input("Оберіть пункт меню: ")

    try:
        if choice == "1":
            for key, value in sport_types.items():
                print(key, "-", value)
        elif choice == "2":
            for surname, fullname in trainers.items():
                print(surname, "-", fullname)
        elif choice == "3":
            for sport, time in schedule.items():
                print(sport, ":", time)
        elif choice == "4":
            for sport, price in prices.items():
                print(sport, ":", price, "грн")
        elif choice == "5":
            surname = input("Введіть прізвище тренера: ")
            coach = find_coach(surname)
            print("Знайдено тренера:", coach)
        elif choice == "0":
            print("Завершення програми.")
            break
        else:
            print("Невірний пункт меню.")

    except CoachNotFoundError as e:
        print("Помилка:", e)