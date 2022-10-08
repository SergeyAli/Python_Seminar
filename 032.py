# Задайте последовательность чисел.Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

numbers = list(map(int, input('Введите последовательность чисел через пробел ').split()))
#numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)


# Если нужно из сиска убрать повторяюхиеся элементы во всех случаях

converted_list = list(map(int, input().split()))
filtered_list = list(filter(lambda x: converted_list.count(x) == 1, converted_list))
print(filtered_list)


