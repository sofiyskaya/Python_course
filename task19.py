# 19. Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

my_list = [i for i in range(10)]
print(my_list)
shift = int(input('Enter the number by which you want to shift the sequence: '))

for _ in range(shift):
    my_list.insert(0, my_list.pop())

print(my_list)    