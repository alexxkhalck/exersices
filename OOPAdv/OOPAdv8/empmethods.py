import datetime
from employees import employees_list

spme = datetime.date.year

def finding_60_65(some_list: list)->int:
    res = 0
    for item in some_list:
        age = datetime.date.today().year - item.date_of_employment.year
        if item.sex == "male" and age > 65 or item.sex == "female" and age > 60:
            res += 1
    return res

print(f"Кількість працівників пенсійного віку: {finding_60_65(employees_list)}")