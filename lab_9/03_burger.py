#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает ингридиентов - создать соответствующие функции в модуле my_burger

import my_burger

def double_cheeseburger():
    my_burger.add_bun()
    my_burger.add_mayones()
    my_burger.add_cotlet()
    my_burger.add_cheese()
    my_burger.add_cotlet()
    my_burger.add_cucumber()
    my_burger.add_tomato()
    my_burger.add_mayones()
    my_burger.add_bun()
    return 0


def gamburger():
    my_burger.add_bun()
    my_burger.add_mayones()
    my_burger.add_cotlet()
    my_burger.add_cucumber()
    my_burger.add_tomato()
    my_burger.add_mayones()
    my_burger.add_bun()
    return 0

double_cheeseburger()

    
    