__all__ = ['select', 'table', 'add']


def select(line, flights):
    """Выбор рейсов по типу самолёта"""
    nom = input('Введите тип желаемого самолёта: ')
    count = 0
    print(line)
    print(
        '| {:^4} | {:^20} | {:^15} | {:^16} |'.format(
            "№",
            "Место прибытия",
            "Номер самолёта",
            "Тип"))
    print(line)
    for i, num in enumerate(flights, 1):
        if nom == num.get('value', ''):
            count += 1
            print(
                '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                    count,
                    num.get('stay', ''),
                    num.get('number', ''),
                    num.get('value', 0)))
    print(line)
    if count == 0:
        print('Таких рейсов нет')


def table(line, flights):
    """Вывод скиска рейсов"""
    print(line)
    print(
        '| {:^4} | {:^20} | {:^15} | {:^16} |'.format(
            "№",
            "Место прибытия",
            "Номер самолёта",
            "Тип"))
    print(line)
    for i, num in enumerate(flights, 1):
        print(
            '| {:<4} | {:<20} | {:<15} | {:<16} |'.format(
                i,
                num.get('stay', ''),
                num.get('number', ''),
                num.get('value', 0)
            )
        )
    print(line)


def add(flights):
    """Добавление нового рейса"""
    value = input('Введите тип самолёта: ')
    number = input('Введите номер самолёта: ')
    stay = input('Введите место прибытия: ')
    air = {
        'number': number,
        'stay': stay,
        'value': value
    }
    flights.append(air)
    if len(flights) > 1:
        flights.sort(key=lambda x: x.get('stay', ''))
