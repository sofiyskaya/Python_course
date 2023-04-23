# Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

list_size = int(input("Enter a length of the list: "))
value = int(input("Enter the number: "))

list_1 = [random.randint(1, 100) for i in range(list_size)]

print(*list_1)

count = 0
for i in range(list_size):
    if list_1[i] == value:
        count += 1

print("The number", value, "is found", count, "times in the list")