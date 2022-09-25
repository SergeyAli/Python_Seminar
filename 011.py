# 11.	Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

print('Введите N ');
N = int(input())
from random import randint
l = [randint(-99,99) for x in range(N)]
print(l)