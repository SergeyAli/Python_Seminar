# 35.	В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его

path = 'list.txt'  # путь к папке
data = open(path, 'r')  # откроем в режиме чтения
list_number = data.readline()
data.close()
list_number = list(map(int, list_number.split()))
print(list_number)

for i in range(1, len(list_number)):
    if not list_number[i] -1 == list_number[i-1]:
        print(f" {list_number[i] -1}")
