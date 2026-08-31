import datetime
from car import Car
from car import cars_list

def find_one_year(some_list: list[Car])->list[Car]:
    today = datetime.date.today()
    res = list(filter(lambda x: today - x.inspection_date > datetime.timedelta(days=365), some_list))
    return res

def main():
    for item in find_one_year(cars_list):
        print(str(item))

if __name__ == "__main__":
    main()