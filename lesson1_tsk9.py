"""
Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).

БЛОК-СХЕМА
https://drive.google.com/file/d/1hQbswLD8yMijpIXCYFu8Tfkxm0a0EfdI/view?usp=sharing
"""

print('Введите три разных числа')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

""" Поиск максимального числа"""

max_num = a
if max_num < b:
    max_num =b
if max_num < c:
    max_num = c

""" Поиск минимального числа"""

min_num = a
if min_num > b:
    min_num = b
if min_num > c:
    min_num = c

""" Поиск среднего числа"""

mdl_num = a
if mdl_num != max_num:
    if mdl_num == min_num:
        mdl_num = b
        if mdl_num == max_num:
            mdl_num =c
print(f'Среднее число: {mdl_num}')
