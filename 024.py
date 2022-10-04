# 24.В заданном списке вещественных чисел найдите разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

arr1 = [1.1, 1.2, 3.1, 5, 10.01]
arr =[]
for i in arr1:
    i=i%1
    arr.append(i)
    i+=1
min=max=arr[0]
for i in arr:
    if i == 0:
        continue
    a = i - float(i)
    if float(i) > max:
        max = float(i)
    elif float(i) < min:
        min = float(i)
print("%.2f" % (max-min))

