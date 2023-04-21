#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить список всех живущих на районе (пакет district) и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
from district.central_street.house1 import room1 as cs11
from district.central_street.house1 import room2 as cs12
from district.central_street.house2 import room1 as cs21
from district.central_street.house2 import room2 as cs22
from district.soviet_street.house1 import room1 as cc11
from district.soviet_street.house1 import room2 as cc12
from district.soviet_street.house2 import room1 as cc21
from district.soviet_street.house2 import room2 as cc22

print("На районе живут " + ", ".join(map((lambda n: n), cs11.folks + cs12.folks 
                                         + cs21.folks + cs22.folks 
                                         + cc11.folks + cc12.folks
                                         + cc21.folks + cc22.folks)))