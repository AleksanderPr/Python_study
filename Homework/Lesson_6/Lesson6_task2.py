

# 2. Реализовать класс Road (дорога).
# ●	определить атрибуты: length (длина), width (ширина);
# ●	значения атрибутов должны передаваться при создании экземпляра класса;
# ●	атрибуты сделать защищёнными;
# ●	определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ●	использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# ●	проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_road_mass(self, thick=1, consumption=20):
        road_mass = self._length * self._width * thick * consumption
        return road_mass


r = Road(length=20, width=5000)
print(r.get_road_mass(thick=5, consumption=25))