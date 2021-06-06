
# 4.	Реализуйте базовый класс Car.
# ●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# ●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ●	для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go_car(self):
        print(f'Машина {self.name} поехала')

    def stop_car(self):
        print(f'Машина {self.name} остановилась')

    def turn_car(self, direction):
        print(f'Машина {self.name} повернула на'+direction)

    def show_speed(self, current_speed):
        print(f'Скорость в настоящее время равноа {current_speed} км в час')


car1 = Car(speed=150, color='red', name='Mazda')
# car1.go_car()
# car1.turn_car('право')
# car1.go_car()
# car1.stop_car()


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, current_speed):
        print(f'Скорость в настоящее время равноа {current_speed} км в час')
        if current_speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, current_speed):
        print(f'Скорость в настоящее время равноа {current_speed} км в час')
        if current_speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



tc1 = TownCar(speed=100, color='grey', name='Opel')
# tc1.go_car()
# tc1.turn_car('право')
# tc1.go_car()
# tc1.stop_car()
# tc1.show_speed(40)
# tc1.show_speed(80)


sc1 = SportCar(speed=300, color='yellow', name='Bugatti')
# sc1.go_car()
# sc1.turn_car('право')
# sc1.go_car()
# sc1.stop_car()
# print(f'Спорткар {sc1.is_police}')



wc1 = WorkCar(speed=90, color='green', name='Kamaz')
# wc1.go_car()
# wc1.turn_car('право')
# wc1.go_car()
# wc1.stop_car()
wc1.show_speed(90)



pc1 = PoliceCar(speed=180, color='blue', name='bmw', is_police=True)
# pc1.go_car()
# pc1.turn_car('право')
# pc1.go_car()
# pc1.stop_car()
# print(pc1.is_police)
# pc1.show_speed(40)
# pc1.show_speed(110)
