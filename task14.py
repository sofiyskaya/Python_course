# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Enter the number N: '))

value = 1

while value < n:
    print(value, end = ' ')
    value *= 2
    
print("\n")    