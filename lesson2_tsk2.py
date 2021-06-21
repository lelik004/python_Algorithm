"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = int(input('Введите число\n'))
even_count, not_even_count = 0, 0

while num > 0:
    last_dgt = num % 10
    if last_dgt % 2 == 0:
        even_count += 1
    else:
        not_even_count += 1
    num = num // 10

print(f'Чётные цифры в числе {even_count}\n'
      f'Нечётные цифры в числе {not_even_count}')
