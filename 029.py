# 29.	Найти НОК двух чисел
# 1 варинат
# x = int(input('Введите первое число: '))
# y = int(input('Введите второе число: '))
# if x > y:
#     nok = x
# else:
#     nok = y
# print
# while True:
#     if nok % x == 0 and nok % y == 0:
#         break
#     nok += 1
# print(f'НОК для чисел {x} и {y} равно {nok}')

# 2 вариан

n = 4
n1 = 6
if n > n1:
    maximum = n
else:
    maximum = n1

if maximum % n == 0 and maximum % n1 == 0:
    print(f"НОК = {maximum}")
else:
    list_n = []
    list_n1 = []
    for i in range(2, n1 + 1):
        list_n.append(n * i)
        list_n1.append(n1 * i)
    noc = 0
    for i in list_n:
        for j in list_n1:
            if i == j:
                noc = i
                print("noc", noc)
                exit()
    if noc == 0:
        noc = n1 * n
    print((f"НОК = {n1 * n}"))
    print(list_n)
    print(list_n1)



