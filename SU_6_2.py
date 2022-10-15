# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



# from dataclasses import replace
from random import randint, choice

pp = '2*х^2 + 4*х + 5 = 0'
pol = ['2','*x^','2',' + ', '4', '*x + ','5',' = 0']

k = 2

ratios = [str(randint(0, 101)) for x in range(k)]
indexes = [0, 4, 6, 2]

def change_poly(pol, indexes, ratios, k):
    ratios.append(str(k))
    for indexes, replacement in zip(indexes, ratios):
        pol[indexes] = replacement
    return "".join(pol)

pol_new = change_poly(pol, indexes, ratios, k)
print(pol_new)

# В одну строку

def change_polynomial(pol, k, rat, ind):
    new_pol = []
    rat.append(str(k))
    new_pol = [ratios[ind.index(i)] if i in ind else pol[i] for i in range(len(pol))]
    return "".join(new_pol)

new_pol = change_polynomial(pol, k, ratios, indexes)
print(new_pol)

with open('SU_6_2_pol_uncorr.txt', 'w') as data:
    data.write(pol_new)