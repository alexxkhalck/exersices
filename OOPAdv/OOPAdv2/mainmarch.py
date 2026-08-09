from merchandise import merch_list

def decorator_names_pc(fn):
    def wrapper(*args):
        jaja = fn(*args)

        for j in jaja:
            print(j)

        return jaja
    return wrapper


def decorator_average_price(fn):
    def wrapper(*args):
        res = fn(*args)
        print(f'Середня вартість: {res}')
        return res
    return wrapper

@decorator_average_price
def average_price(some_list):
    average = lambda items: sum(item.cost for item in items) / len(items)
    return average(some_list)

@decorator_names_pc
def names_of_pc(some_list):
    res_list = list(map(lambda x: x.name, some_list))
    return res_list

result = average_price(merch_list)

res_names = names_of_pc(merch_list)