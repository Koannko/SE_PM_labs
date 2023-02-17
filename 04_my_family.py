#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append('Anna')
my_family.append('Sveta')
my_family.append('Sasha')
my_family.append('Slava')


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 169],
    [my_family[1], 162],
    [my_family[2], 187],
    [my_family[3], 178],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("Рост отца - %d см" % my_family_height[2][1])
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
