"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Сумма места, занимаемого переменными: 2116

"""

import random
import sys


def how_much(obj, sum_mem):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    sum_mem_aux = sys.getsizeof(obj)
    if hasattr(obj, '__iter__'):
        for items in obj:
            print(f'{type(items)=}, {sys.getsizeof(items)=}, {items=}')
            if hasattr(items, '__iter__'):
                for item in items:
                    print(f'{type(item)=}, {sys.getsizeof(item)=}, {item=}')
                    sum_mem_aux += sys.getsizeof(item)
            sum_mem_aux += sys.getsizeof(items)
    sum_mem += sum_mem_aux
    print(f'{sum_mem_aux=}, {sum_mem=}')
    return sum_mem

COLUMN, ROW = 4, 4
START = -100
FINISH = 100

sum_main = 0
sum_main += how_much(COLUMN, sum_main) + how_much(ROW, sum_main)\
            + how_much(START, sum_main) + how_much(FINISH, sum_main)

matrix = [[random.randint(START, FINISH) for _ in range(COLUMN)] for _ in range(ROW)]
matrix_2 = []
row_min = []

sum_main = how_much(matrix, sum_main)

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

sum_main = how_much(matrix_2, sum_main)
#   Составим список из минимальных элементов каждого столбца.

for i in matrix_2:
    min_el = FINISH
    for el in i:
        if el < min_el:
            min_el = el
    row_min.append(min_el)

sum_main = how_much(row_min, sum_main)

max_of_min = row_min[0]

for el in row_min:
    if el > max_of_min:
        max_of_min = el

sum_main = how_much(max_of_min, sum_main)

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_of_min}')
print(f'\nСумма места, занимаемого переменными: {sum_main}\n')
