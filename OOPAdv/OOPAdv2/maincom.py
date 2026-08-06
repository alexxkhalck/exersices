from  commodity import commodity_list

def commodity_decorator(fn):
    def wrapper(*args, **kwargs):
        result = list(filter(lambda x: x.price == fn(commodity_list), commodity_list))
        return result
    return wrapper

@commodity_decorator
def the_most_expensive_commodity(some_list):
    y = max(x.price for x in some_list)
    return y

#print(the_most_expensive_commodity(commodity_list))
for item in the_most_expensive_commodity(commodity_list):
    print(item)