
# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __add__(self, other):
        return Complex(self.param1 + other.param1, self.param2 + other.param2)

    def __mul__(self, other):
        return Complex(self.param1 * other.param1 - self.param2 * self.param2,
                       self.param1 * other.param2 + self.param2 * other.param1)

    def __str__(self):
        return f'{self.param1} + {self.param2}i'

comlex_num1 = Complex(4, 5)
comlex_num2 = Complex(-3, 6)
print('Сложение', comlex_num1 + comlex_num2)
print('Произведение', comlex_num1 * comlex_num2)
