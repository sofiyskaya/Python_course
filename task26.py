# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

number = int(input('Введите число: '))
degree = int(input('Укажите степень: '))
def pow(number, degree):

    if degree == 0:
        return 1
    else:
        return number * pow(number, degree-1)

print(pow(number,degree))