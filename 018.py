# 18.	# Реализовать алгоритм перемешивания списка.
number = [1, 2, 8, 6, 5, 7, 12, 55]
print(number)
for i in range(0, int(len(number)//2)):
    number[i], number[len(number)-i - 1] = number[len(number)-i - 1], number[i]

print(number)



