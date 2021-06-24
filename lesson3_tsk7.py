"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random

START = 0
FINISH = 100
LENGTH = 10

main_list = [random.randint(START, FINISH) for _ in range(LENGTH)]
min_el1 = FINISH
min_el2 = FINISH
print(f'Исходный массив: {main_list}')

if main_list[0] <= main_list[1]:
    min_el1, min_el2 = main_list[0], main_list[1]
else:
    min_el1, min_el2 = main_list[0], main_list[1]

for j in range(2, len(main_list)):
    if main_list[j] <= min_el1:
        temp = min_el1
        min_el1 = main_list[j]
        if temp < min_el2:
            min_el2 = temp
    elif main_list[j] < min_el2:
        min_el2 = main_list[j]

print(f'Минимальный элемент 1: {min_el1}\nМинимальный элемент 2: {min_el2}')
