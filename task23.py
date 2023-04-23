# 23. Дан список, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов списка, больших предыдущего (элемента с предыдущим номером)

import random
list_input = [random.randint(0, 5) for i in range(5)]
print (list_input)
count=0
for i in range(len(list_input)-1):
    if list_input[i] < list_input[i+1]: 
        count+=1
print(count)