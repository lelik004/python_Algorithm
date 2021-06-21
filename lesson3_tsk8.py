"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

r_count = 1
last_clm = []
row_sum = 0
matrix_1 = []
matrix_2 = []


print('Введите числа матрицы через пробел. Для перехода на новую строку нажмите Enter')
while r_count <= 4:
    row = input()
    matrix_1.append(row.split(' '))
    r_count += 1

#   Сформируем матрицу 2 размер 4*4, которая потом станет финальной размером 5*4

for i in matrix_1:
    row_ = [int(j) for j in i]
    matrix_2.append(row_)

#   Создадим спискок. Каждый элемент равен сумме элементов строки.

for i in matrix_2:
    for j in i:
        row_sum += int(j)
    last_clm.append(row_sum)
    row_sum = 0


#   Добавим элементы в последний стобец.

for el in range(len(matrix_2)):
    matrix_2[el] += [last_clm[el]]


print('Исходная матрица:')
for rw in matrix_1:
    for el in rw:
        print(f'{el:>5}', end='')
    print()

print('Финальная матрица:')
for rw in matrix_2:
    for el in rw:
        print(f'{el:>5}', end='')
    print()
