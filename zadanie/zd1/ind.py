#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from function import main


"""
Используя замыкания функций, объявите внутреннюю функцию, которая принимает в
качестве параметров фамилию и имя, а затем, заносит в шаблон эти данные. Сам шаблон –
это строка, которая передается внешней функции и, например, может иметь такой вид:
«Уважаемый %F%, %N%! Вы делаете работу по замыканиям функций.» Здесь %F% - это
фрагмент куда нужно подставить фамилию, а %N% - фрагмент, куда нужно подставить имя.
(Шаблон может быть и другим, вы это определяете сами). Здесь важно, чтобы внутренняя
функция умела подставлять данные в шаблон, формировать новую строку и возвращать
результат. Вызовите внутреннюю функцию замыкания и отобразите на экране результат ее
работы.
"""


if __name__ == '__main__':
    print(main()(input('Введите фамилию: '), input('Введите имя: ')))
