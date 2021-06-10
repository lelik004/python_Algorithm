"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
проходящей через эти точки.

БЛОК-СХЕМА
https://drive.google.com/file/d/1hQbswLD8yMijpIXCYFu8Tfkxm0a0EfdI/view?usp=sharing
"""
print('Введите координаты точки A')
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
print('Введите координаты точки B')
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))

if x1 != x2:
    k = (y1 - y2)/(x2 - x1)
    b = y1 - k * x1
    print(f'Уравнение прямой проходящей через точки A и B: y = {k} * x + {b}')
else:
    print('Координаты точек А и В по оси абсцисс равны.\nСоставить уравнение вида y=kx+b невозможно.')
