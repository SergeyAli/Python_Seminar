# 29.	Найти НОК двух чисел
n = 2
n1 = 5
if n > n1:
    maximum = n
else:
    maximum = n1

if maximum % n == 0 and maximum % n1 == 0:
    print(f"НОК = {n1}")
else:
    print(f"НОК = {n1 * n}")
