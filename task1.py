#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
#При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

n = int(input('Введите сколько машина проезжает за день: '))
m = int(input('Введите сколько нужно проехать: '))

result = (n - 1 + m) // n
print(result)