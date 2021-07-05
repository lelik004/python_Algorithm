import random

array = [random.randint(-100, 99) for _ in range(10)]
len_array = len(array)
print(f'Исходный массив: {array}')

n = 1
while n < len_array:
    count = 0
    for i in range(len_array - 1):
        if array[i] < array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            count += 1
    if count == 0:
        break
    n += 1

print(f'Отсортированный массив: {array}')
