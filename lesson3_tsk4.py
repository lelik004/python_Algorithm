"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

START = 0
FINISH = 100
LENGTH = 100

main_list = [random.randint(START, FINISH) for _ in range(LENGTH)]
print(f'Исходный массив: {main_list}')

count = 0
max_count = 0
max_count_el = 0

for i in main_list:
    for j in main_list:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        max_count_el = i
    count = 0

print(f'Число {max_count_el} встречается чаще всего в исходном массиве чисел.')
