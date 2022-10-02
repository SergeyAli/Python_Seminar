# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# 1 Вариант
# print('Введите N ');
# N = int(input())
# umbers = list(range(1, N+1))
# for i in umbers:
#     print(f"{umbers[i-1]} : {3*i+1}", end = ", ")
#
# # 2 Вариант
# n = int(input('N = '))
# d = {}
# for i in range(1, n+1):
#     d.update({i: 3*i + 1})
# print(d)

# 3 Вариант

n = int(input('N = '))
d = {}
for i in range(1, n+1):
    d.setdefault(i, 3*i + 1)
print(d)
