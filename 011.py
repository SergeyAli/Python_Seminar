# 11.	Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
N = int(input('Введите N '))
# print('Введите N ');
# N = int(input())
# from random import randint
# l = [randint(-99,99) for x in range(N)]
# print(l)
# matrix = []
# for i in range(n):
#     matrix.append((-3)**i)
# print(f"Итоговая последовательность: {matrix}")
start = 1
for i in range(1, N+1):
    print(start, end=' ')
    start *= -3