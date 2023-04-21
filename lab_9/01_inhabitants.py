#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...
import room_1
import room_2
print("В комнате room_1 живут: " + ", ".join(map((lambda n: n), room_1.folks)) +
      "\nВ комнате room_2 живут: " + ", ".join(map((lambda n: n), room_2.folks)))
