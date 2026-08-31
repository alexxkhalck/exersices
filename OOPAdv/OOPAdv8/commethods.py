import datetime
from commodity import com_list
from commodity import Commodity

def search_expiration_com(some_list: list[Commodity])->float:
    res = 0.0
    for item in some_list:
        if item.expiration_date < datetime.date.today():
            res = res + item.price * item.quantity
    return res

def main():
    print(f"Загольна сума простроченого товару: {search_expiration_com(com_list)}")

if __name__ == "__main__":
    main()