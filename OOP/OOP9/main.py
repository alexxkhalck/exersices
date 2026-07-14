from methods import searching_prod
from methods import read_from_file
from methods import amount_of_ram
from methods import read_from_file_prod
from arrayofobj import products
from arreyofprod import shopprod

choice = int(input('Ви бажаєте перевірити першу задачу, чи другу? '))

match choice:
    case 1:
        searching_prod(products)
        read_from_file()
    case 2:
        amount_of_ram(shopprod)
        read_from_file_prod()