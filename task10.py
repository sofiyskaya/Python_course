# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

import random

n = int(input('Enter the number of coins: '))

a = 0
b = 0
i = 0

for i in range(n):
    coin_side= random.randint(0, 1)
    print(coin_side)
    if coin_side == 0:
        a += 1
    if coin_side == 1:
        b += 1
print(f'all coins {a, b}')

if a > b:
    min_value = b
else:
    min_value = a

print(f'The minimum value of coins, that you need to flip {min_value}')        