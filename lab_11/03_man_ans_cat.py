# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint
# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.
class Cat():

    def __init__(self, name = 'Tomato'):
        self.name = name
        self.fullness = 50
        self.house = None

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        if self.is_alive():
            cprint('{} поспал'.format(self.name), color='blue')
            self.fullness -= 10

    def make_mess(self):
        if self.is_alive():
            self.house.dirt += 5
            self.fullness -= 10
            cprint('{} подрал обои'.format(self.name), color='grey')

    def is_alive(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return False
        return True

    def act(self):
        if not self.is_alive():
            return False
        
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.make_mess()
        else:
            self.sleep()

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def take_cat(self, cat):
        cat.house = self.house

    def buy_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кошачьей едой'.format(self.name), color='magenta')
            self.house.money -= 20
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cleanup(self):
        if self.house.dirt >= 100:
            self.house.dirt -= 100
            self.fullness -= 20
            cprint('{} убрался в доме'.format(self.name), color='green')
        else:
            cprint('{} в доме итак чисто!'.format(self.name), color='red')

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return False
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.cat_food < 10:
            self.buy_cat_food()
        elif self.house.dirt >= 100:
            self.cleanup()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды для человека осталось {}\n, еды для кота осталось {}\n, уровень грязи {}\n, денег осталось {}'.format(
            self.food, self.cat_food, self.dirt, self.money)


# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код

days_left = 365
Snow = Cat('Snow')
John = Man('John')
sweet_home = House()
John.house = sweet_home

# John.take_cat(Snow)
# while days_left:
#     if John.act():
#         break
#     if Snow.act():
#         break
#     days_left -= 1


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.
Tom = Cat('Tom')
# Trisha = Cat('Trisha')
John.take_cat(Tom)
# John.take_cat(Trisha)

John.take_cat(Snow)
while days_left:
    John.act()
    Snow.act()
    Tom.act()
    # Trisha.act()
    days_left -= 1

# (Можно определить критическое количество котов, которое может прокормить человек...)
