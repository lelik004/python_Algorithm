import random


def merge_sort_fst_step(lst):
    if len(lst) < 2:
        return lst
    else:
        mdl = len(lst) // 2
        left_part = merge_sort_fst_step(lst[:mdl])
        right_part = merge_sort_fst_step(lst[mdl:])
        return merge_sort_snd_step(left_part, right_part)


def merge_sort_snd_step(left_part, right_part):
    result = []
    i, j = 0, 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            result.append(left_part[i])
            i += 1
        else:
            result.append(right_part[j])
            j += 1
    while i < len(left_part):
        result.append(left_part[i])
        i += 1
    while j < len(right_part):
        result.append(right_part[j])
        j += 1
    return result


array = [round(random.random() * 50, 5) for _ in range(10)]
print(f'Исходный массив: {array}\n'
      f'Отсортированный массив: {merge_sort_fst_step(array)}')
