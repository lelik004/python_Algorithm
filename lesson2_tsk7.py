"""
Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""


def equal(n, sum_left, sum_right, count):
    if n != 0:
        if count != n:
            count += 1
            if count <= n:
                sum_left += count
        else:
            sum_right = int(count * (count + 1) / 2)
            print(f'Для уравнения 1+2+...+n = n(n+1)/2\n'
                  f'Сумма правой части = {sum_right}\n'
                  f'Сумма левой части = {sum_left}')
            if sum_left == sum_right:
                print('Тождество верно')
            else:
                print('Тождество неверно')
    else:
        return print('0=0 и нечего тут доказывать')
    return equal(n, sum_left, sum_right, count)


n = int(input('Введите число: '))
sum_left, sum_right, count = 0, 0, 0
equal(n, sum_left, sum_right, count)

