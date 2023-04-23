# Требуется найти в cписке A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

list_size = int(input("Enter a length of the list: "))
value = int(input("Enter a value from 1 to 100: "))

list_1 = [random.randint(1, 100) for i in range(list_size)]

print(*list_1)

min_diff = 100
value_index = 0
for i in range(list_size):
    cur_diff = abs(list_1[i] - value)
    if cur_diff < min_diff:
        min_diff = cur_diff
        value_index = i

print("The nearest number to", value, "is the element: ", value_index + 1, " - ", list_1[value_index])