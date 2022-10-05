# 23.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]

if len(list) % 2 == 0:
    # print('Chet')
    for i in range(0, int(len(list) // 2)):
        b = list[i] * list[len(list) - i - 1]
        print(b, end=' ')
else:
    # print('Nechet')
    for i in range(0, int((len(list)//2))+1):
        b=list[i] *list[len(list)-i - 1]
        print(b, end=' ')