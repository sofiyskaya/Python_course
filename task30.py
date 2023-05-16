# Задача 30:  
# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input("Enter the first element of progression: "))
step = int(input("Enter the step of the progression: "))
size = int(input("Enter the number of element to print: "))

print(f"\n arithmetic progression:\n{[i for i in range(first_element, first_element + (size * step), step)]}")