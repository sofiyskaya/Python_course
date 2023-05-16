# Задача No33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

import random

marks = [random.randint(1, 5) for _ in range(10)]
print(marks)

max_mark = max(marks)
print(max_mark)

min_mark = min(marks)
print(min_mark)

for i in range (len(marks)):
    if marks[i] == max_mark: marks[i] = min_mark
print(marks)    