# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код
# sd.resolution = (800, 800)
def draw_branches(start_point, start_angle, branch_length):
    if branch_length < 10:
        return
    start_point = sd.vector(start_point, start_angle, branch_length)
    
    draw_branches(start_point, start_angle + 30, branch_length * 0.75)
    draw_branches(start_point, start_angle - 30, branch_length * 0.75)

# root_point = sd.get_point(300, 30)
# draw_branches(root_point, 90, 100)

# sd.pause()

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
sd.resolution = (800, 800)
def draw_branches_hardlevel(start_point, start_angle, branch_length):
    if branch_length < 10:
        return
    start_point = sd.vector(start_point, start_angle, branch_length)
    
    alpha = 30 * sd.random_number(0, 40) / 100
    branch_length *= 0.75 * sd.random_number(0, 20) / 100    
    draw_branches_hardlevel(start_point, start_angle + alpha, branch_length)
    draw_branches_hardlevel(start_point, start_angle - alpha, branch_length)

root_point = sd.get_point(300, 30)
draw_branches_hardlevel(root_point, 90, 100)

sd.pause()
