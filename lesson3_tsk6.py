"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

START = 0
FINISH = 100
LENGTH = 20

main_list = [random.randint(START, FINISH) for _ in range(LENGTH)]
max_el = START
min_el = FINISH
sum_el = 0
print(f'Исходный массив: {main_list}')

for i in main_list:
    if i > max_el:
        max_el = i
        index_max = main_list.index(i)
    if i < min_el:
        min_el = i
        index_min = main_list.index(i)

print(f'max = {max_el},\nmin = {min_el}')

if index_min < index_max:
    for i in main_list[index_min + 1: index_max]:
        sum_el += i
else:
    for i in main_list[index_max + 1: index_min]:
        sum_el += i

print(f'Сумма элементов между max и min: {sum_el}')
