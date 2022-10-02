# 29.	Найти НОК двух чисел
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
    for i in range(2, n1+1):
        list_n.append(n*i)
        list_n1.append(n1 * i)
    for i in list_n:
        noc = 0
        for j in list_n1:
            if i == j:
                noc = i
                break
    if noc == 0:
        noc = n1 * n
    print((f"НОК = {n1 * n}"))
    print(list_n)
    print(list_n1)
