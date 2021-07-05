"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Более оптимальный вариант.
Сумма места, занимаемого переменными: 9084.
Убрал Deque, добавил один кортеж.

MacOS, 64bit
Python 3.8.5
"""

from functools import reduce
import sys


def how_much(obj, sum_mem):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    sum_mem_aux = sys.getsizeof(obj)
    if hasattr(obj, '__iter__'):
        for items in obj:
            print(f'{type(items)=}, {sys.getsizeof(items)=}, {items=}')
            sum_mem_aux += sys.getsizeof(items)
    sum_mem += sum_mem_aux
    print(f'{sum_mem_aux=}, {sum_mem=}')
    return sum_mem


def indx_sum(a, b):
    sum_ab = []
    cnt = 0
    for i, j in zip(a, b):
        sum_ab += [i + j]
        cnt += 1
    if len(a) > len(b):
        sum_ab += a_indx[cnt:]
    elif len(b) > len(a):
        sum_ab += b_indx[cnt:]

    return sum_ab


def incrs_bit(num_lst, sum_main_, cnt=0):
    aux_num_lst = num_lst[::-1]
    for dg in aux_num_lst:
        if dg / 16 >= 1:
            if (cnt + 1) == len(aux_num_lst):     # Добавляем цифру в начале в случае повышения разряда последенго элемента.
                aux_num_lst.append(0)
            aux_num_lst[cnt] = dg % 16
            aux_num_lst[cnt + 1] += dg // 16
        else:
            aux_num_lst[cnt] = dg
        cnt += 1
    sum_main_ = how_much(aux_num_lst, sum_main_)
    return aux_num_lst, sum_main_


def list_to_hex(num_not_hex, sum_main_):
    hex_lst_func = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    hex_num = ''
    for el in num_not_hex[::-1]:
        hex_num += hex_lst_func[el]
    sum_main_ = how_much(hex_lst_func, sum_main_)
    sum_main_ = how_much(hex_num, sum_main_)
    return hex_num, sum_main_


# Получение индексов цифр каждого числа в списке 0-F в hex_lst.
def hex_to_indx(xf, yf, sum_main_):
    a_index = []
    b_index = []
    for k in xf:
        a_index.append(HEX_LST.index(k))
    for j in yf:
        b_index.append(HEX_LST.index(j))
    sum_main_ = how_much(a_index, sum_main_)
    sum_main_ = how_much(b_index, sum_main_)
    return a_index, b_index, sum_main_


HEX_LST = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

sum_main = 0
sum_main = how_much(HEX_LST, sum_main)

# x = input('Введите первое число: ')
# y = input('Введите второе число: ')
# x = '20A4'
# y = 'c15'
x = 'A2'
y = 'C4F'
# x = '1C52'
# y = '891'

# xd = collections.deque(x.upper())
# yd = collections.deque(y.upper())
xd = [_ for _ in x.upper()]
yd = [_ for _ in y.upper()]

sum_main = how_much(xd, sum_main)
sum_main = how_much(yd, sum_main)


"""
Сложение
"""
# Уравнивание длины символов чисел
if len(xd) > len(yd):
    for _ in range(len(xd) - len(yd)):
        yd.insert(0, '0')
elif len(xd) < len(yd):
    for _ in range(len(yd) - len(xd)):
        xd.insert(0, '0')

sum_main = how_much(xd, sum_main)
sum_main = how_much(yd, sum_main)

# Получение индексов цифр каждого числа в списке 0-F в hex_lst.
a_indx, b_indx, sum_main = hex_to_indx(xd, yd, sum_main)

sum_main = how_much(a_indx, sum_main)
sum_main = how_much(a_indx, sum_main)

# Сложение индесков цифр каждого числа
sum_of_indx_sum = indx_sum(a_indx, b_indx)

sum_main = how_much(sum_of_indx_sum, sum_main)

# Получение корректного индекса цифры числа
num_crct_indx_sum, sum_main = incrs_bit(sum_of_indx_sum, sum_main)

sum_main = how_much(num_crct_indx_sum, sum_main)

# Перевод числа в HEX
sum_xy, sum_main = list_to_hex(num_crct_indx_sum, sum_main)

sum_main = how_much(sum_xy, sum_main)

"""
Умножение чисел
"""
# xd = collections.deque(x.upper())
# yd = collections.deque(y.upper())
xd = [_ for _ in x.upper()]
yd = [_ for _ in y.upper()]

sum_main = how_much(xd, sum_main)
sum_main = how_much(yd, sum_main)

# Получение индексов цифр каждого числа в списке 0-F в hex_lst.
a_indx, b_indx, sum_main = hex_to_indx(xd, yd, sum_main)

sum_main = how_much(a_indx, sum_main)
sum_main = how_much(a_indx, sum_main)

# Поэлементное перемножение индексов чисел
mult_list = []
first_num = a_indx
second_num = b_indx
if len(b_indx) > len(a_indx):
    first_num, second_num = b_indx, a_indx
for i in second_num[::-1]:
    mult = [i * j for j in first_num]
    mult_list.append(mult)

sum_main = how_much(mult_list, sum_main)
sum_main = how_much(first_num, sum_main)
sum_main = how_much(first_num, sum_main)
sum_main = how_much(first_num, sum_main)
sum_main = how_much(mult, sum_main)
sum_main = how_much(len(b_indx), sum_main)
sum_main = how_much(len(b_indx), sum_main)

# Добавление, при необходимости, '0' в начало каждого получившегося числа для сложения столбиком.
count = 0
aux_list = mult_list[::-1]
for num in aux_list:
    if count > 0:
        for _ in range(count):
            num.insert(0, int('0'))
        aux_list[count] = num
    count += 1

sum_main = how_much(count, sum_main)
sum_main = how_much(aux_list, sum_main)

# Уравниваем колчисетво цифр в разных числах перед сложением. То есть добавляем '0' в конце числа
max_num_len = len(aux_list[0])
for num in aux_list:
    if len(num) > max_num_len:
        max_num_len = len(num)
for num in aux_list:
    if len(num) < max_num_len:
        for _ in range(max_num_len - len(num)):
            num.append(int('0'))

sum_main = how_much(max_num_len, sum_main)
sum_main = how_much(len(num), sum_main)

# Складываем получившиеся после поэлементного перемножения числа.
sum_of_indx_mult = reduce(indx_sum, aux_list)

sum_main = how_much(sum_of_indx_mult, sum_main)

# Проход по всем элементам списка суммы с целью повышения разряда.
num_crct_indx_mult, sum_main = incrs_bit(sum_of_indx_mult, sum_main)

sum_main = how_much(num_crct_indx_mult, sum_main)

# Перевод числа в списке в соответствующие числа в шестнадцатеричной системе счисления.
mult_xy, sum_main = list_to_hex(num_crct_indx_mult, sum_main)

sum_main = how_much(mult_xy, sum_main)

print(f'Сложение числа {x} и {y} равно {sum_xy}')
print(f'Умножение числа {x} на {y} равно {mult_xy}')
print(f'\nСумма места, занимаемого переменными: {sum_main}\n')
