# Записывать данные в файл
# with open('file.txt', 'a') as data: #
#    data.write('line 1\n')
#    data.write('line 2\n')

# colors = ['red', 'green', 'blue'] # список с данными
# data = open('file.txt', 'w') # созаем текстовую еременную data и связаваем ее с текстовым файлом file.txt, указваем мод а - дозапись w- запись r - чтение
# data.writelines(colors) # разделителей не будет data.close()
# data.close()

# colors = ['red', 'green', 'blue'] # список с данными
# data = open('file.txt', 'a')
# data.writelines('\nLINE14\n')
# data.write('LINE15\n')
# data.close()
#exit() # позволяет не выполнять код после  нее

# Читать данные из файла
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# ФУНКЦИИ

# import Lek_1 # Импротипровали  функцию из файла Lek_1
#
# print(Lek_1.f(1)) # Обратились к функции F и выполнилиее

# можно прописать алиас что бы не писать полностью имя файла и путь к нему

# import Lek_1 as h
#
# print(h.f(1))

# передаца нескольких аргументов
# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
#
# print(concatenatio('a', 's', 'd', 'w'))	# asdw
# print(concatenatio('a', '1', 'd', '2'))	# a1d2

# print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# РЕКУРСИЯ

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34


# КОРТЕЖИ

# a, b = 3, 4 # множественное присвоение
# (a, b) = (3, 4) # а это уже КОРТЕЖ

a=(3, 1, 41, 4)

# print(a)
# print(a[0])

# for item in a:
#     print (item)


# t = tuple(['red', 'green', 'blue'])
# print(t[0])  # red
# print(t[2])  # blue
# # print(t[10])	# IndexError: tuple index out of range
# print(t[-2])  # green
# # print(t[-200]) # IndexError: tuple index out of range
#
# for e in t:
#     print(e)  # red green blue
#
# t[0] = 'black'# TypeError: 'tuple' object does not support item assignment

# РАСПАКОВАТЬ КОРТЕЖ В ОТДЕЛЬНЫЕ ПЕРЕМЕННЫЕ


# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

#  СЛОВАРИ

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary['up'])  # ↑
# # типы ключей могут отличаться
#
# dictionary['left'] = '⇐'
# print(dictionary['left'])  # ⇐
# # print(dictionary['type'])	# KeyError: 'type'
# del dictionary['left']  # удаление элемента
# for item in dictionary:  # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
#
# # up: ↑
# # down: ↓
# # right: →

# МНОЖИСТВО

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a))	# set
# print(type(b))	# set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a))  # set
# print(type(b)) # set
# print(type(c))  # set
# a = {1, 1, 1, 1, 1}
# print(a)  # {1}



colors = {'red', 'green', 'blue'}
print(colors)  # {'red', 'green', 'blue'}
colors.add('red') # добовлять, если такой элемент есть то не добавляеться
print(colors)  # {'red', 'green', 'blue'}
colors.add('gray') # добовлять
print(colors)  # {'red', 'green', 'blue','gray'}
colors.remove('red') # удолять
print(colors)  # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red' - если элемента не будет в множестве то будет ошибка
colors.discard('red')  # ok
print(colors)  # {'green', 'blue','gray'}
colors.clear()  # { } # очищять
print(colors)  # set()


a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()		# c = {1,	2,	3,	5,	8}
u = a.union(b)		# u = {1,	2,	3,	5,	8,	13,	21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}

q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

# Неизменяемое множество

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

# СПИСКИ











