"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import cProfile
from timeit import timeit
import random

"""
Вариант 1
"""
def matrix(n):
    COLUMN, ROW = n * 4, n * 4
    START = -n * 100
    FINISH = n * 100
    clm = 0

    matrix = [[random.randint(START, FINISH) for _ in range(COLUMN)] for _ in range(ROW)]
    matrix_2 = []
    row_min = []

    # print('Исходная матрица:')
    # for rw in matrix:
    #     for el in rw:
    #         print(f'{el:>5}', end='')
    #     print()

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

"""
Вариант 2
Другой способ переворота матрицы.
"""

def matrix2(n):
    COLUMN, ROW = n * 4, n * 4
    START = -n * 100
    FINISH = n * 100
    clm = 0

    matrix = [[random.randint(START, FINISH) for _ in range(COLUMN)] for _ in range(ROW)]
    matrix_2 = []
    row_min = []

    # print('Исходная матрица:')
    # for rw in matrix:
    #     for el in rw:
    #         print(f'{el:>5}', end='')
    #     print()

    #   Перевернем матрицу.
    for i in range(len(matrix[0]), 0, -1):
        matrix_2.append(list(map(lambda x: x[i - 1], matrix)))

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

    # print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_of_min}')


"""
Вариант 3
Другой способ переворота матрицы + использования max и min функций
"""


def matrix3(n):
    COLUMN, ROW = n * 4, n * 4
    START = -n * 100
    FINISH = n * 100
    clm = 0

    matrix = [[random.randint(START, FINISH) for _ in range(COLUMN)] for _ in range(ROW)]
    matrix_2 = []
    row_min = []

    # print('Исходная матрица:')
    # for rw in matrix:
    #     for el in rw:
    #         print(f'{el:>5}', end='')
    #     print()

    #   Перевернем матрицу.
    for i in range(len(matrix[0]), 0, -1):
        matrix_2.append(list(map(lambda x: x[i - 1], matrix)))

    for i in matrix_2:
        min_el = min(i)
        row_min.append(min_el)

    max_of_min = max(row_min)

    # print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_of_min}')


print('n  Вариант №1  Вариант №2  Вариант №3')

for n in range(1, 51, 5):
    tt1 = timeit('matrix(n)', number=1000, globals=globals())
    tt2 = timeit('matrix2(n)', number=1000, globals=globals())
    tt3 = timeit('matrix3(n)', number=1000, globals=globals())
    print(f'{n}  {tt1:.7f}   {tt2:.7f}   {tt3:.7f}')

cProfile.run('matrix(100)')
cProfile.run('matrix2(100)')
cProfile.run('matrix3(100)')

# matrix3(1)

"""
Результаты тестов не сильно отличаются друг от друга. Первый вариант чуть-чуть побыстрее.
Третий вариант на удивление второй по быстродействию, хотя там добавляются встроенные функции min и max.
Я подразумевал, что это увеличит время время выполнения.

На мой взгляд варианты 1 и 3 более оптимальны. Особенно вариант 3, так как он более читаемый и понятный для меня, 
хоть и менее быстродейственный. 

n  Вариант №1  Вариант №2  Вариант №3
1   0.0522846    0.0494070    0.0529805
6   1.3065085    1.4538865    1.4550385
11  4.2430173    4.4118057    4.4047314
16  8.4661912    8.8477692    8.8070789
21  15.6119866   15.8662963   15.9809743
26  23.4240568   24.0976433   23.8388074
31  32.1788308   33.0814017   33.3131057
36  43.2020601   44.4791621   44.1416984
41  59.7247826   61.4307859   61.4413986
46  74.1796732   77.0165805   76.4352822
"""

