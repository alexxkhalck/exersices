# Написати функцію, яка за допомогою регулярних виразів з файлу витягує дані про дату народження, телефон та електронну адресу.
# Дані потрібно записати до іншого файлу.
from methodstask2 import *

ivaniv = ['Ivanov', '12.06.2001', '+380222222222', '222@gmail.com']
pavlov = ['Pavlov', '13.07.2002', '+380333333333', '333@gmail.com']
andreev = ['Andreev', '14.08.2003', '+380444444444', '444@gmail.com']
user_list = [ivaniv, pavlov, andreev]

writing_to_file(user_list)

res_list = iter(read_from_file())

get_data(res_list)