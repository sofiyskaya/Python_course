# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Дляэтого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

from math import sqrt

s = int(input('Enter the sum of numbers: '))
p = int(input('Enter the multiplication of numbers: '))

if s > 0 and p > 0 and s <= 2000 and p <= 1000000:
    res = sqrt((s/2) ** 2 - p)
    print(f'The values are: {int(s/2 - res), int(s/2 + res)}')
else:
    print('The values are not in range!')    