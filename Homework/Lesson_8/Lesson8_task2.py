
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

param_1 = int(input("Введите делимое: "))
param_2 = int(input("Введите делитель: "))

try:
    result = param_1 / param_2
except ZeroDivisionError:
    print("Делить на ноль нельзя")
else:
    print(f"Результат: {result}")
