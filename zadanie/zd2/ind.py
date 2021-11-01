#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from moduls import *


def main():
    flights = []
    print('Список комманд: \n exit - Завершить работу'
          ' \n add - Добавить рейс \n'
          ' list - Показать список рейсов'
          ' \n select - Выбрать рейсы по типу самолёте')
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 20,
        '-' * 15,
        '-' * 16
    )
    while True:
        com = input('Введите команду: ').lower()
        if com == 'exit':
            break
        elif com == "add":
            add(flights)
        elif com == 'list':
            table(line, flights)
        elif com == 'select':
            select(line, flights)
        else:
            print(f"Неизвестная команда {com}", file=sys.stderr)


if __name__ == '__main__':
    main()
