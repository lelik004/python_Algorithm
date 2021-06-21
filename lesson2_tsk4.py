"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


def sum_of_row(num, num_in_row, sum_num, cnt):
    if num > 0:
        if cnt != num:
            sum_num += num_in_row
            cnt += 1
            num_in_row = (-1) * num_in_row / 2
        else:
            return sum_num
    else:
        sum_num = 0
    return sum_of_row(num, num_in_row, sum_num, cnt)


n = int(input('Введите количество чисел: '))
first_num = 1
sum_of_num = 0
count = 0
print(sum_of_row(n, first_num, sum_of_num, count))
