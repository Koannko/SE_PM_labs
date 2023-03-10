#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
centre_bubble = sd.get_point(100, 500)
for i in range(3):
    sd.circle(center_position=centre_bubble, radius=i*5+20)
# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код
def bubbles(centre_circle=sd.get_point(300, 500), color_circle=sd.COLOR_BLUE, radius_circle=25,
           step=10):
    for _ in range(3):
        sd.circle(center_position=centre_circle, radius=radius_circle, color=color_circle)
        radius_circle += step
bubbles()
# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for i in range(10):
    centre_bubble = sd.get_point((500 + 50 * i), 500)
    sd.circle(center_position=centre_bubble, radius=20)
# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
for i in range(3):
    for j in range(10):
        centre_bubble = sd.get_point((100 + 50 * j), 300 - 50 * i)
        sd.circle(center_position=centre_bubble, radius=20)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for i in range(100):
    centre = sd.random_point()
    radius = random.randint(5, 50)
    color = sd.random_color()
    sd.circle(center_position=centre, radius=radius, color=color)
sd.pause()