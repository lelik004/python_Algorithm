"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

START = 0
FINISH = 100
LENGTH = 10

main_list = [random.randint(START, FINISH) for _ in range(LENGTH)]
max_el = START
min_el = FINISH
print(f'Исходный массив: {main_list}')

for i in main_list:
    if i > max_el:
        max_el = i
    if i < min_el:
        min_el = i

index_max = main_list.index(max_el)
index_min = main_list.index(min_el)

main_list[index_min], main_list[index_max] = main_list[index_max], main_list[index_min]

print(f'max = {max_el}\nmin = {min_el}\nИзмененный массив: {main_list}')
