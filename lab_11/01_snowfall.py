# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
width = 800
height = 800

class Snowflake:
    def __init__(self, height, width):
        self.length = sd.random_number(10, 100)
        self.x = sd.randint(10, width - 10)
        self.y = height + sd.randint(100, 400)
        self.factor_a = sd.random_number(4, 7) / 10
        self.factor_b = sd.random_number(4, 7) / 10
        self.factor_c = sd.random_number(45, 60)
    
    def move(self):
        self.x -= sd.randint(-5, 5)
        self.y -= sd.randint(10, 15)

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(
            point, self.length,
            sd.COLOR_WHITE,
            self.factor_a,
            self.factor_b,
            self.factor_c)
    
    def can_fall(self):
        if self.y >= -10:
            return True
        return False
    
    def clear_previous_picture(self):
        sd.start_drawing()
        sd.clear_screen()

    # TODO здесь ваш код


flake = Snowflake(height, width)

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
