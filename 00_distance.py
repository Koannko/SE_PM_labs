#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

len = len(sites)
x1 = 0
x2 = 0
y1 = 0
y2 = 0
distances = {}
directions = {}
for n in range(len):
    x1 = sites.get(list(sites.keys())[n])[0]
    y1 = sites.get(list(sites.keys())[n])[1]
    for k in range(len):
        x2 = sites.get(list(sites.keys())[k])[0]
        y2 = sites.get(list(sites.keys())[k])[1]
        if (n != k):
            directions[list(sites.keys())[k]] = (
                (x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            distances["%s" % (list(sites.keys())[n])] = directions
    directions = {}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# TODO здесь заполнение словаря

print(distances)
