# Задать список из n чисел последовательности(1 +〖1 / n)〗 ^ n и вывести на экран их сумму


print('Введите N ');
n = int(input())
N = list(range(1, n+1))
sum_N=0
for i in N:
    sum_N += (1 + (1 / i)) ** i
    print(f"{sum_N}",  end = ", ")

