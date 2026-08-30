from merchlist import merch_list
from merch import Merchandice

def average_cost(some_list: list[Merchandice])->float:
    res = sum(map(lambda x: x.cost, some_list))/len(some_list)
    return res

def names_and_costs(some_list: list[Merchandice])->list:
    res = list(map(lambda x: (x.name, x.cost), some_list))
    return res


def main():

    average = average_cost(merch_list)
    names_costs = names_and_costs(merch_list)
    print(f"Середня вартість: {average}")
    print("Names of the PCs and their costs.")
    for item in names_costs:
        print(f"Name: {item[0]}, Cost: {item[1]}")

if __name__ == "__main__":
    main()