#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)-1
if(month % 7 % 2 == 0):
    print(31)
elif(month == 1):
    print(28)
else:
    print(30)

# TODO здесь ваш код
