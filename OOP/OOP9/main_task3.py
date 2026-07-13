from pathlib import Path
from task3 import simple_numbers
from task3 import write_in_file
from task3 import read_from_file

input_number = int(input('Введіть кількість чисел: '))
path_list = Path(__file__).parent/"file_simple_nums.txt"

res = simple_numbers(input_number)

write_in_file(res, path_list)

ask = input('Ви бажаєте вивести на екран список чисел?')
if ask.lower() in ('y', 'yes'):
    read_from_file(path_list)