"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.

БЛОК-СХЕМА
https://drive.google.com/file/d/1hQbswLD8yMijpIXCYFu8Tfkxm0a0EfdI/view?usp=sharing
"""
year = int(input('Введите год: '))
if year % 4 != 0 or (year % 400 != 0 and year % 100 == 0):
    print('Введенный год не високосный')
else:
    print('Введенный год високосный')
