#  Задача No37. Решение в группах
# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

num = int(input('Enter the number: '))

def reverse_sequence(n: int):
    if n == 1:
        return n
    else:
        return f'{n} {reverse_sequence(n - 1)}'
    
print(reverse_sequence(num))