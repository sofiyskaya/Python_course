#  Задача No35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

def prime_num (n, div):
    if div == n//2 + 1:
        print('yes')
    elif n % div == 0:
        print('no')
    else:
        prime_num(n, div + 1)

value = int(input('Enter the number: '))
prime_num(value, 2)