"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

START = -100
FINISH = 100
LENGTH = 100

main_list = [random.randint(START, FINISH) for _ in range(LENGTH)]
print(f'Исходный массив: {main_list}')

max_neg_el = START
count = 0
for i in main_list:
    if 0 > i >= max_neg_el:
        max_neg_el = i
        count += 1

if count == 0:
    print('Отрицательных элементов нет')

print(f'Максимальный отрицательный элемент в массиве равен {max_neg_el}')
