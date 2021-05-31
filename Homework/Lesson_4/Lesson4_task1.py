
# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.


import sys
arguments = sys.argv

if len(arguments) < 2:
    print('Запустите скрипт в терминале')
def payment():
    try:
        working_hours = int(arguments[1])
        pay_rate = int(arguments[2])
        bonus = int(arguments[3])
        result = working_hours * pay_rate + bonus
        print(f'Заработная плата соторудника сставит: {result}')
    except (IndexError, ValueError):
        print('Введите количество отработанных часов.')
        print('Далее через пробел введите ставку за час рабочего времени,')
        print('и затем также через пробел размер премии')

payment()
