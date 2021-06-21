"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

БЛОК-СХЕМА
https://drive.google.com/file/d/1hQbswLD8yMijpIXCYFu8Tfkxm0a0EfdI/view?usp=sharing
"""
num_letter = int(input('Введите номер буквы: '))
dictionary = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
    11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
    21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
}
letter = dictionary.get(num_letter)
print(letter)
