#По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
#Решить задачу используя цикл while

number = int(input('Enter the number: '))

fact = 1
i = 1

while i <= number:
    fact *= i
    i += 1

print(fact)    