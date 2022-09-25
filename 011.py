# 11.	Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
N = int(input('Введите N '))

start = 1
for i in range(1, N+1):
    print(start, end=' ')
    start *= -3