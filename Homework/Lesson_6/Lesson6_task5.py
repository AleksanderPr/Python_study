

# 5.Реализовать класс Stationery (канцелярская принадлежность).
# ●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# ●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ●	в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# ●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.



class Stationery:
    def __init__(self, title):
        self.title = title


    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw_pen(self):
        print('Ручка пишет')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw_pencil(self):
        print('Карандаш чертит')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw_handle(self):
        print('Маркер подчеркивает')

s = Stationery('brush')
s.draw()
#
pen = Pen('pen')
pen.draw_pen()

pencil1 = Pencil('pencil')
pencil1.draw_pencil()

h1 = Handle('handle')
h1.draw_handle()