# 41. Дан список, состоящий из целых чисел. 
# Напишите программу, которая в данном списке определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.

import random

list_first = [random.randint(0, 10) for _ in range(10)]
print(list_first)

print(len([i for i in range(1, len(list_first) - 1) if list_first[i - 1] < list_first[i] > list_first[i + 1]]))
