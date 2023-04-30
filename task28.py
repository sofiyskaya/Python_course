# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

first_num = int(input('Enter the first number: '))
second_num = int(input('Enter the second number: '))
def sum(first_num, second_num):
    if second_num == 0:
        return first_num
    return sum(first_num + 1, second_num - 1)
print(f'The sum of entered numbers - {sum(first_num, second_num)}')