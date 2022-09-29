# print ('hello мир')
# value = None
# print (type(value))
from tkinter import Variable


a = 123
b = 1.23
# print (a)
# print (b)
# print (type(a))
# print (type(b))
# value = 12345
# print (type(value))
s = ' Hello  world'
# ss = 'Hello "world'
# sss = "Hello 'world"
# ssss = 'Hello \'world'

# print (a, '-', b, '-', s) # Вывод строки
# print ('{} - {} - {}'.format (a,b,s)) # Вывод строки формат
# print (f'{a} - {b} - {s}') # Вывод строки инторполяция
# print ('{2} - {0} - {1}'.format (a,b,s)) # Вывод строки формат

# f = True
# print (f)

# list = ['1', '2', '3']
# print (list)

# print ('Введите a');
# a = int (input ())
# print ('Введите b');
# b = int (input ())
# print (a, ' + ', b, ' = ', a+b)
# # print ('{} {}'.format (a, b))
# # print (f'{a} {b}')


# print ('Введите a');
# a = float (input ())
# print ('Введите b');
# b = float (input ())
# print (a, ' + ', b, ' = ', a+b)
# # print ('{} {}'.format (a, b))
# # print (f'{a} {b}')


#  Арефметические действия

# a = 1.3123223
# b = 3
# c = round(a * b, 5)
# print (c)

#  Присваевание

# a = 3
# a = a + 5  # Одинаковые выражения
# a += 5

# Логические операции

# a = 1 > 4
# print (a)

# a = [1, 2]
# b = [1, 2]
# print (a == b)

# a = 1 < 3 < 5  # Можно использовать тройные неравенства
# print (a)

# f = 1>2 or 4< 5  # or  - или
# print (f)

# f = [1, 2, 3, 4]  # in - в
# print (2 in f)

# Опредиление четности числа

# is_odd = f[0] % 2 == 0 # Одинаковые выражения
# is_odd = not f[0] % 2
# print (is_odd)

# Управляющие конструкции
#1

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print (b)

#2

# username = input('Введите имя ')
# if username == 'Маша':
#     print ('Ура, это же Маша!')
# elif username == 'Марина':
#     print ('Я так ждал Вас, Марина!')
# elif username == 'Ильнар':
#     print ('Ильнар - тор')
# else:
#     print ('Привет, ', username)

# Управляющие конструкции: while-else
# Переворот числа

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)
# Пожалуй
# хватит )
# 32

# Управляющие конструкции: for

# for i in 1, -2, 3, 14, 5:
#     print (i**2)

# list = [1, -2, 3, 14, 5]
# for i in list:
#     print (i**2)

# r = range(10)
# for i in r:
#     print (i)

# for i in range(5):
#     print (i)

# for i in range(1, 10, 2):
#     print (i)


# Немного о строках

# text = 'съешь ещё этих мягких французских булок'
# print(len(text))                 # 39 len - подсчет количство символов
# print('ещё' in text)             # True in - проверяет присутствует ли слово в тексте
# print(text.isdigit())            # False isdigit - проеряет числа ли в строках
# print(text.islower())            # True  islower - проверяет нижнир регистер
# print(text.replace('ещё','ЕЩЁ')) #

# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])   # c
# print(text[1])   # ъ
# print(text[len(text)-1])  # к
# print(text[-5])  # б
# print(text[:])   # print(text)
# print(text[:2])  # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# Списки: введение
# Список – пронумерованная,
# изменяемая коллекция объектов произвольных типов

# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]

# ran = range(1,6)
# print(ran)  # приведение тира range к типу list

# umbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]

# for i in numbers:
#     i *= 2
#     print(i)     # [20, 4, 6, 8, 10]
# print(numbers)   # [10, 2, 3, 4, 5]




# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e) # red green blue

# for e in colors:
#     print(e*2)  # redred greengreen blueblue

# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент


# Функции
# Это фрагмент программы, используемый многократно

def f(x):
    return x**2


def f(x):                   #print(f(1))         # Целое
    if x == 1:              #print(f(2.3))       # 23
        return 'Целое'      #print(f(28))        # None
    elif x == 2.3:          #print(type(f(1)))   # str
        return 23           #print(type(f(2.3))) # int
    else:                   #print(type(f(28)))  # NoneType
        return
arg = 2.3
print(f(arg))
print(type(f(arg)))

