"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

num = int(input('Введите число: '))
reverse_num = 0

while num > 0:
    last_dgt = num % 10
    reverse_num =(reverse_num + last_dgt) * 10
    num = num // 10

reverse_num = reverse_num // 10
print(f'Обратное число: {reverse_num}')

