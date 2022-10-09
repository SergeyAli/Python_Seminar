# Вычислить число π c заданной точностью d
# Пример: при d = 0.001, π = 3.141.10 ^ (-1)≤d≤10 ^ (-10)


import math
precision = int(input("Задайте точностью вывода от 1 до 10 знаков после запятой "))
while precision > 50:
	print("Число слишком большое")
	precision = int(raw_input("Сколько знаков? "))
else:
	print('%.*f' % (precision, math.pi))