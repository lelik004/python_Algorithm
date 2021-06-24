"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

COLUMN, ROW = 4, 4
START = -100
FINISH = 100

matrix = [[random.randint(START, FINISH) for _ in range(COLUMN)] for _ in range(ROW)]
matrix_2 = []
row_min = []

print('Исходная матрица:')
for rw in matrix:
    for el in rw:
        print(f'{el:>5}', end='')
    print()

clm = 0

#   Перевернем матрицу.

while clm != COLUMN:
    matrix_2.append([matrix[j][clm] for j in range(len(matrix))])
    clm += 1

#   Составим список из минимальных элементов каждого столбца.

for i in matrix_2:
    min_el = FINISH
    for el in i:
        if el < min_el:
            min_el = el
    row_min.append(min_el)


max_of_min = row_min[0]

for el in row_min:
    if el > max_of_min:
        max_of_min = el

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_of_min}')
