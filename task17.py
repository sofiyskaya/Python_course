# Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

import random
list_input = [random.randint(-5, 5) for i in range(10)]
print(list_input)
set_output = set(list_input)
print(len(set_output))