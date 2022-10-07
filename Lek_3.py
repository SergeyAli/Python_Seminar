
# def f(x):
#     x**2
# g = f
#
# print(f(1))
# print(g(1))

# def f(x):
#     return x**2
# g = f
#
# print(type(f))
# print(type(g))
#
# print(f(4))
# print(g(4))

# def calc1(x):
#     return x+10
#
# # print(calc1(10))
#
# def calc2(x):
#     return x*10
#
# # print(calc2(10))
#
# def math(op, x):
#     print(op(x))
#
# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):
#     return x+y
# f=sum  # можно переписать проще
# sum = lambda x, y: x+y +1

# def mylt(x, y):
#     return x*y
#
# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)
#
# # calc(mylt, 4, 5)
# # calc(sum, 4, 5)
# # calc(f, 4, 5)
# # calc(sum, 4, 5)
# calc(lambda x, y: x+y +1, 4, 5)

# Четные числа в диопазоне от 1 до 100

# 1 Variant
list = []

# for i in range(1, 101):
#     if(i%2 ==0):
#         list.append(i)
# print(list)

#  2 Variant

# for i in range(1, 101):
#     # if(i%2 ==0):
#     list.append(i)
# print(list)

#  3 Variant

# list = [i for i in range(1, 21) if(i%2 ==0)]
# print(list)

# пары чисел - кортежи
# list = [(i, i) for i in range(1, 21) if(i%2 ==0)]
# print(list)

# List Comprehension
# def f(x):
#     return x**3
# list = [(i, f(i)) for i in range(1, 21) if(i%2 ==0)]
# print(list)


# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа). Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
#
# def f(x):
#     return x**3
# list = [(i, f(i)) for i in list1 if(i%2 ==0)]
# print(list)

# ХРЕН ЗНАЧИТ ЧТО ТАКОЕ В ЛЕНЦИИ

# path = 'file.txt'
# f=open(path, 'r')
# data=f.read() + ""
# f.close()
#
# numbers = []
#
# while data !='':
#     space_pos = data.index('')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1]
#
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e,e **2))
# print(out)

# Улудшение
# def select(f, col):
#     return [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# Решение с смпользованием функции map
# ПРИ ЗАПУСКЕ ОШИБКА
# li = [x for x in range(1,20)]
#
# li = list(map(lambda x:x+10, li)) # в  писке каждое число увеличиваем на 10
#
# print(li)

# ее варианты
# data= list(map(int,input().split())) # НЕ РАБОТАЕТ
# print(data)
# data = list(map(int,'1 2 3 4 5'.split()))
# for e in data:
#     print(e)
# print('--')
# for e in data:
#     print(e)
# Улудшение преведушей задачи используя map

# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = map(int, data)
# res = where(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

data = [x for x in range(10)]

res = list(filter(lambda x: x%2==0, data))
print(res)
