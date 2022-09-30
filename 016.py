# Задать список из n чисел последовательности(1 +〖1 / n)〗 ^ n и вывести на экран их сумму

# print('Введите N ');
# N = int(input())
# umbers = list(range(1, N+1))
# for i in umbers:
#     print(f"{umbers[i-1]} : {3*i+1}", end = ", ")

# n = 5
# lst = [i] * (1+(1/n))**n
# print(lst)


print('Введите N ');
N = int(input())
sum_N = list(range(1, N+1))
f=0
for i in sum_N:
    f += (1 + (1 / i)) ** i
    print(f"{f}",  end = ", ")

