# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
width = 800
height = 800
sd.resolution = (width, height)

class Snowflake:
    def __init__(self, height, width):
        self.length = sd.random_number(10, 100)
        self.x = sd.randint(10, width - 10)
        self.y = height + sd.randint(0, 800)
        self.factor_a = sd.random_number(4, 7) / 10
        self.factor_b = sd.random_number(4, 7) / 10
        self.factor_c = sd.random_number(45, 60)
    
    def move(self):
        self.x -= sd.randint(-5, 5)
        self.y -= sd.randint(0, 10)

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(
            point, self.length,
            sd.COLOR_WHITE,
            self.factor_a,
            self.factor_b,
            self.factor_c)
    
    def can_fall(self):
        if self.y >= -self.length - 10:
            return True
        return False
    
    def clear_previous_picture(self):
        # sd.start_drawing()
        sd.clear_screen()
    # TODO здесь ваш код


# flake = Snowflake(height, width)

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
def get_flakes(plan = 10):
    produced = 0
    stock = []
    while produced < plan:
        new_flake = Snowflake(height, width)
        stock.append(new_flake)
        produced += 1
    return stock
        
fallen_flakes = 0

def append_flakes(flakes, fallen_flakes):
    return flakes + get_flakes(fallen_flakes)
count = 0
flakes = get_flakes()  # создать список снежинок
sd.start_drawing()
while True:
    for flake in flakes:
        flake.draw()
        flake.move()
        if not flake.can_fall():
            fallen_flakes += 1
    sd.sleep(0.05)
    sd.finish_drawing()  # подчитать сколько снежинок уже упало
    sd.clear_screen()
    if fallen_flakes > count:
        flakes = append_flakes(flakes, fallen_flakes)  # добавить еще сверху
    count = fallen_flakes
    fallen_flakes = 0
    if sd.user_want_exit():
        break

sd.pause()
