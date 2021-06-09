# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, п
# роверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Absrtact(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def get_consumption(self):
        pass

class Coat(Absrtact):
    def __init__(self, param):
        super().__init__(param)
    @property
    def get_consumption(self):
        return (self.param / 6.5 + 0.5)


class Suit(Absrtact):
    def __init__(self, param):
        super().__init__(param)
    @property
    def get_consumption(self):
        return (self.param *2 + 0.3)

coat1 = Coat(50)
print(f'Пртребление материала на поальто: {coat1.get_consumption}')

suit1 = Suit(40)
print(f'Пртребление материала на костюм: {suit1.get_consumption}')







