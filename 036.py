# 36.	Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя


list01 = [1, 5, 2, 3, 4, 6, 1, 7]
list01 = list(map(int, list01))

#k = 0
for i in range(len(list01)):
    list02 = []
    list02.append(min(list01))
    for j in range(i, len(list01)):
        if list02[-1] < list01[j]:
            #k += 1
            list02.append(list01[j])
    print(list02)

