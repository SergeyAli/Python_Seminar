# 22.	Найти сумму чисел списка стоящих на нечетной позиции

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Элементы списка:")
print(myList)
list_length = len(myList) # Функция len() считает количество элементов списка

sumOfElements = 0
count = 1 # Задаем переменную счётчика. 1 – потому что суммируем с нечетной позиции
while count < list_length:
    sumOfElements = sumOfElements + myList[count]
    count += 2 # Счётчик крутим через одну позицию, тем самым проходимся по нечетным позициям

print("Сумма всех элементов списка:", sumOfElements)