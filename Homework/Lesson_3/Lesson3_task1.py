
# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.



def division():
    arg1 = int(input('Введите делимое '))
    arg2 = int(input('Введите делитель '))
    try:
        result = arg1 / arg2
    except ZeroDivisionError:
        return print(f'Деление на ноль')
    return result


print(f'результат равен: {division()}')
