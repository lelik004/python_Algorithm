import random


def create_heap(lst, heap_size, root_index):
    largest_indx = root_index
    left_child_indx = root_index * 2 + 1
    right_child_indx = root_index * 2 + 2
    if left_child_indx < heap_size and lst[left_child_indx] > lst[largest_indx]:
        largest_indx = left_child_indx
    if right_child_indx < heap_size and lst[right_child_indx] > lst[largest_indx]:
        largest_indx = right_child_indx
    if largest_indx != root_index:
        lst[root_index], lst[largest_indx] = lst[largest_indx], lst[root_index]
        create_heap(lst, heap_size, largest_indx)


def heap_sort(lst):
    len_lst = len(lst)

    for i in range(len_lst, -1, -1):
        create_heap(lst, len_lst, i)

    for i in range(len_lst - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        create_heap(lst, i, 0)
    return lst


array = [random.randint(0, 99) for _ in range(11)]
array_sort = heap_sort(array)
mdl = len(array_sort) // 2
median = array_sort[mdl]
print(f'Исходный массив: {array}\n'
      f'Отсортированный массив: {array_sort}\n'
      f'Медиана: {median}')
