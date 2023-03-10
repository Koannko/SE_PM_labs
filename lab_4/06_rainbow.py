#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.
x1, y1, x2, y2 = 50, 50, 350, 450
width = 4
for color_item in rainbow_colors:
    start_point = sd.get_point(x1, y1)
    end_point = sd.get_point(x2, y2)
    sd.line(start_point=start_point, end_point=end_point, color=color_item, width=width)
    x1 += 5
    x2 += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
x_center, y_center = 600, -100
center_position = sd.get_point(x_center, y_center)
radius = 400
width = 10
for color_item in rainbow_colors:
    sd.circle(center_position=center_position, radius=radius, color=color_item, width=width)
    radius -= -11
sd.pause()
