# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

number = int(input('Enter the number: '))

i = 1
fib = 0
prev = 0

while fib < number:
    if i == 1:
        fib = 0
    if i == 2:
        prev = 0
        fib = 1

    tmp = fib
    fib += prev
    prev = tmp

    i += 1

if number == fib:
    print(i)
else:
    print(-1)


