"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections
from functools import reduce


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


def incrs_bit(num_lst, cnt=0):
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
    return aux_num_lst


def list_to_hex(num_not_hex):
    hex_lst_func = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hex_num = ''
    for el in num_not_hex[::-1]:
        hex_num += hex_lst_func[el]
    return hex_num


# Получение индексов цифр каждого числа в списке 0-F в hex_lst.
def hex_to_indx(xf, yf):
    a_index = []
    b_index = []
    for k in xf:
        a_index.append(HEX_LST.index(k))
    for j in yf:
        b_index.append(HEX_LST.index(j))
    return a_index, b_index


HEX_LST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


x = input('Введите первое число: ')
y = input('Введите второе число: ')
# x = '20A4'
# y = 'c15'
# x = 'A2'
# y = 'C4F'
# x = '1C52'
# y = '891'

xd = collections.deque(x.upper())
yd = collections.deque(y.upper())


"""
Сложение
"""
# Уравнивание длины символов чисел
if len(xd) > len(yd):
    for _ in range(len(xd) - len(yd)):
        yd.appendleft('0')
elif len(xd) < len(yd):
    for _ in range(len(yd) - len(xd)):
        xd.appendleft('0')


# Получение индексов цифр каждого числа в списке 0-F в hex_lst.
a_indx, b_indx = hex_to_indx(xd, yd)

# Сложение индесков цифр каждого числа
sum_of_indx_sum = indx_sum(a_indx, b_indx)

# Получение корректного индекса цифры числа
num_crct_indx_sum = incrs_bit(sum_of_indx_sum)

# Перевод числа в HEX
sum_xy = list_to_hex(num_crct_indx_sum)

"""
Умножение чисел
"""
xd = collections.deque(x.upper())
yd = collections.deque(y.upper())

# Получение индексов цифр каждого числа в списке 0-F в hex_lst.
a_indx, b_indx = hex_to_indx(xd, yd)

# Поэлементное перемножение индексов чисел
mult_list = []
first_num = a_indx
second_num = b_indx
if len(b_indx) > len(a_indx):
    first_num, second_num = b_indx, a_indx
for i in second_num[::-1]:
    mult = [i * j for j in first_num]
    mult_list.append(mult)

# Добавление, при необходимости, '0' в начало каждого получившегося числа для сложения столбиком.
count = 0
aux_list = mult_list[::-1]
for num in aux_list:
    if count > 0:
        for _ in range(count):
            num.insert(0, int('0'))
        aux_list[count] = num
    count += 1


# Уравниваем колчисетво цифр в разных числах перед сложением. То есть добавляем '0' в конце числа
max_num_len = len(aux_list[0])
for num in aux_list:
    if len(num) > max_num_len:
        max_num_len = len(num)
for num in aux_list:
    if len(num) < max_num_len:
        for _ in range(max_num_len - len(num)):
            num.append(int('0'))


# Складываем получившиеся после поэлементного перемножения числа.
sum_of_indx_mult = reduce(indx_sum, aux_list)

# Проход по всем элементам списка суммы с целью повышения разряда.
num_crct_indx_mult = incrs_bit(sum_of_indx_mult)

# Перевод числа в списке в соответствующие числа в шестнадцатеричной системе счисления.
mult_xy = list_to_hex(num_crct_indx_mult)

print(f'Сложение числа {x} и {y} равно {sum_xy}')
print(f'Умножение числа {x} на {y} равно {mult_xy}')
