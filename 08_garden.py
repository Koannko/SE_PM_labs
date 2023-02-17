#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка',
          'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка',
          'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)
# выведите на консоль все виды цветов
# TODO здесь ваш код
print(garden_set, meadow_set)
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
both_flowers = []
for i in garden_set:
    for j in meadow_set:
        if (i == j):
            both_flowers.append(i)
print(both_flowers)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
only_meadow_flowers = []

for j in meadow_set:
    if (j not in garden_set):
        only_meadow_flowers.append(j)
print(only_meadow_flowers)
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
only_garden_flowers = []
for i in garden_set:
    if (i not in meadow_set):
        only_garden_flowers.append(i)
print(only_garden_flowers)
