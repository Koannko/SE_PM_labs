# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр 02_global_color.py скопировать сюда
# Результат решения см results/exercise_03_shape_select.jpg

# TODO здесь ваш код
sd.resolution = (800, 800)
colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
colors_names = ['Красный', 'Оранжевый', 'Жёлтый', 'Зелёный', 'Бирюзовый', 'Синий', 'Фиолетовый']
shapes_names = ['Треугольник', 'Квадрат', 'Пятиугольник', 'Шестиугольник']

for i, color in enumerate(colors_names):
    print(i, '-', color)

def user_input_color():
    user_data = input("Введите номер цвета: ")
    color_num = int(user_data)
    if 0 <= color_num < 7:
        print('Вы ввели', color_num)
        return color_num
    else:
        print('Некорректные данные')


user_color = user_input_color()

for j, shape in enumerate(shapes_names):
    print(j, '-', shape)

def user_input_shape():
    user_input1 = input("Введите номер фигуры: ")
    shape_num = int(user_input1)
    if 0 <= shape_num < 4:
        print('Вы ввели', shape_num)
        return shape_num
    else:
        print('Некорректные данные')

user_shape = user_input_shape()

def count_angle(start_point, zero_angle, side_length, sides_count, color_id):
    end_point = start_point
    angle_shift = int(360 / sides_count)
    for angle in range(0, 360 - angle_shift, angle_shift):
        start_point = sd.vector(start_point, angle + zero_angle, side_length, colors[color_id])

    sd.line(start_point, end_point, colors[color_id])


point = sd.get_point(400, 300)
count_angle(start_point=point, zero_angle=45, side_length=200, sides_count=user_shape+3,color_id=user_color)
sd.pause()
