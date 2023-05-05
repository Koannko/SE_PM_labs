# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код

class Element():
    def __add__(self, element):
        if self.name == element.name:
            return self.name

class Water(Element):

    def __init__(self):
        self.name = "Вода"

    def __add__(self, element):
        if element.name == "Воздух":
            return Storm().__str__()
        elif element.name == "Огонь":
            return Couple().__str__()
        elif element.name == "Земля":
            return Dirt().__str__()
        else:
            return super().__add__(element)

    def __str__(self):
        return self.name
    

class Air(Element):

    def __init__(self):
        self.name = "Воздух"

    def __add__(self, element):
        if element.name == "Вода":
            return Storm().__str__()
        elif element.name == "Огонь":
            return Lightning().__str__()
        elif element.name == "Земля":
            return Dust().__str__()
        else:
            return super().__add__(element)

    def __str__(self):
        return self.name
    

class Fire(Element):

    def __init__(self):
        self.name = "Огонь"

    def __add__(self, element):
        if element.name == "Вода":
            return Couple().__str__()
        elif element.name == "Воздух":
            return Lightning().__str__()
        elif element.name == "Земля":
            return Lion().__str__()
        else:
            return super().__add__(element)

    def __str__(self):
        return self.name
    

class Earth(Element):

    def __init__(self):
        self.name = "Земля"

    def __add__(self, element):
        if element.name == "Вода":
            return Dirt().__str__()
        elif element.name == "Воздух":
            return Dust().__str__()
        elif element.name == "Огонь":
            return Lion().__str__()
        else:
            return super().__add__(element)
    def __str__(self):
        return self.name
    



class Storm(Element):

    def __init__(self):
        self.name = "Шторм"

    def ___add__(self, element):
        return super().__add__(element)

    def __str__(self):
        return self.name


class Couple(Element):

    def __init__(self):
        self.name = "Пар"

    def ___add__(self, element):
        return super().__add__(element)

    def __str__(self):
        return self.name
    

class Dirt(Element):

    def __init__(self):
        self.name = "Грязь"

    def ___add__(self, element):
        return super().__add__(element)

    def __str__(self):
        return self.name


class Lightning(Element):

    def __init__(self):
        self.name = "Молния"

    def ___add__(self, element):
        return super().__add__(element)

    def __str__(self):
        return self.name


class Dust(Element):

    def __init__(self):
        self.name = "Пыль"

    def ___add__(self, element):
        return super().__add__(element)

    def __str__(self):
        return self.name


class Lion(Element):

    def __init__(self):
        self.name = "Лава"

    def ___add__(self, element):
        return super().__add__(element)

    def __str__(self):
        return self.name
    


el1 = Couple()
el2 = Couple()
print(el1, '+', el2, '=', el1 + el2)
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
