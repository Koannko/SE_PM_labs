#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать (или при необходимости написать) функции отрисовки
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

from draw.rainbow import *
from draw.smile import *
from draw.snow import *
from draw.tree import *
from draw.wall import *
import math

sd.resolution = (1000, 600)
sd.rectangle(sd.get_point(0, 0), sd.get_point(2000, 100), sd.COLOR_GREEN)
draw_rainbow()
for i in range(50):
    draw_snowflake(200, 100)
draw_tree(sd.get_point(800, 100), 90, 100)
draw_wall(300, 100)
sd.rectangle(sd.get_point(400, 150), sd.get_point(500, 200), sd.COLOR_BLUE)
draw_smile(450, 170, sd.COLOR_YELLOW)
sd.rectangle(sd.get_point(270, 100), sd.get_point(300, 250), sd.COLOR_RED)
sd.rectangle(sd.get_point(600, 100), sd.get_point(620, 250), sd.COLOR_RED)
sd.rectangle(sd.get_point(270, 250), sd.get_point(620, 300), sd.COLOR_RED)
sd.circle(sd.get_point(100, 500), radius=50, color=sd.COLOR_ORANGE, width=50)
for i in range(12):
    start = sd.get_point(100, 500)
    end = sd.get_point(100 + 100 * math.cos(i * 30), 500 + 100 * math.sin(i * 30))
    sd.line(start_point=start, end_point=end, color=sd.COLOR_ORANGE, width=5)


sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
