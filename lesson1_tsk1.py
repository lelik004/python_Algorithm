"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

БЛОК-СХЕМА
https://drive.google.com/file/d/1hQbswLD8yMijpIXCYFu8Tfkxm0a0EfdI/view?usp=sharing
"""
num = int(input('Введите трехзначное число: '))
if 1 <= num / 100 <= 9.99:
    dg1 = num // 100
    dg2 = num // 10 - dg1 * 10
    dg3 = num % 10
    pr_dg = dg1 * dg2 * dg3
    sum_dg = dg1 + dg2 + dg3
    print(f"Произведение цифр числа {num} равно {pr_dg}\nСумма цифр числа {num} равна {sum_dg}")
else:
    print('Введено не трехзначное число')
