#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код
len = len(my_favorite_movies)
name = ''
for n in range(len):
    if (my_favorite_movies[n] != ',' and n != len - 1):
        if (my_favorite_movies[n] != ' '):
            name += my_favorite_movies[n]
        elif (my_favorite_movies[n] == ' ' and my_favorite_movies[n - 1] != ','):
            name += my_favorite_movies[n]
        if (my_favorite_movies[n + 1] == ','):
            print(name)
            name = ''
