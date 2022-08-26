"""
Алгоритм основан на методе расчета расстояния Фреше.
Расчитывается Евклидово расстояние между двумя точками двух траекторий
и набольшее расстояние будет расстоянием Фреше.
Т.к. у нас в данных разное колличество точек, будем брать по наименьшей колличество точек каждой траектории.
"""

from frechetdist import frdist
import pandas as pd


# Создаем словаарь с координатами траекторий
lines = {1: [], 2: [], 3: [], 4: []}

df = pd.read_table('traks.csv', sep=';')

# Заполняем созданный словарь координатами точек траекторий
for row in df.itertuples():
    lines[row.track].append([row.x, row.y])

# Для наглядности пересохраняем их в списки
line1 = lines[1]
line2 = lines[2]
line3 = lines[3]
line4 = lines[4]

print('Анализируем совпадение траектории 3 и траектории 1.')

if len(line1) >= len(line3):
    result = frdist(line1[:len(line3)], line3)
else:
    result = frdist(line3[:len(line1)], line1)

print(result, end='\n\n')

print('Анализируем совпадение траектории 2 и траектории 1.')

if len(line1) >= len(line2):
    result = frdist(line1[:len(line2)], line2)
else:
    result = frdist(line2[:len(line1)], line1)

print(result, end='\n\n')


print('Анализируем совпадение траектории 4 и траектории 1, 2, 3.')

if len(line1) >= len(line4):
    result = frdist(line1[:len(line4)], line4)
else:
    result = frdist(line4[:len(line1)], line1)

print(result, "- с траекторией 1", end='\n\n')


if len(line2) >= len(line4):
    result = frdist(line2[:len(line4)], line4)
else:
    result = frdist(line4[:len(line2)], line2)

print(result, "- с траекторией 2", end='\n\n')

if len(line3) >= len(line4):
    result = frdist(line3[:len(line4)], line4)
else:
    result = frdist(line4[:len(line3)], line3)

print(result, "- с траекторией 3", end='\n\n')