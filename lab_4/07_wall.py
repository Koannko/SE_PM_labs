#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич
sd.resolution = (1050, 500)
for j in range(10):
    for i in range(10):
        start = sd.get_point(i * 130 -j % 2 * 65, j * 60)
        end = sd.get_point(i * 130 + 100 + 20 - j % 2 * 65, j * 60 + 50)
        sd.rectangle(left_bottom=start, right_top=end, color=sd.COLOR_RED)
sd.pause()
