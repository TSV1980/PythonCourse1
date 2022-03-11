"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда);

опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    """ Автомобиль  """

    speed = 0
    """ Скорость    """

    color = 'Red'
    """ Цвет машины """

    name = ''
    """ Название машины """

    is_police = False
    """    Полиция это или нет    """

    def __init__(self, speed, color, name, is_police):
        """_summary_

        Args:
            speed (int): Скорость
            color (str): Цвет машины
            name (str): Название машины
            is_police (bool): Полиция это или нет
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(
            f' Появился автомобиль {self.name}. Его цвет {self.color}. Его скорость {self.speed}. Это полиция? = {self.is_police}')

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name}остановился')

    def turn(self, direction):
        if (direction == 'Right'):
            print(f'Автомобиль {self.name} повернул направо.')
        if (direction == 'Left'):
            print(f'Автомобиль {self.name} повернул налево.')

    def show_speed(self):
        print(f'Текущая скорость автомобиля = {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        # При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
        if int(self.speed) > 60:
            print(f'Внимание! Скорость выше 60 км/ч!')
        return super().show_speed()


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        # При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
        if int(self.speed) > 40:
            print(f'Внимание! Скорость выше 40 км/ч!')
        return super().show_speed()


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, True)


town_car1 = TownCar(45, "Red", "TCarBig", False)
town_car1.go()
town_car1.stop()
town_car1.turn("Left")
town_car1.turn("Right")
town_car1.show_speed()
town_car1.speed = 99
town_car1.show_speed()

print('\r\r')

work_car1 = WorkCar(55, "Green", "TWCar", False)
work_car1.go()
work_car1.stop()
work_car1.turn("Left")
work_car1.turn("Right")
work_car1.show_speed()
work_car1.speed = 99
work_car1.show_speed()

print('\r\r')

police_car1 = PoliceCar(100, "Red", "POLICE", True)
police_car1.go()
police_car1.stop()
police_car1.turn("Left")
police_car1.turn("Right")
police_car1.show_speed()
police_car1.speed = 110
police_car1.show_speed()
police_car1.speed = 120
police_car1.show_speed()

print('\r\r')

sport_car1 = SportCar(200, "Yellow", "Formula-1", False)
sport_car1.go()
sport_car1.stop()
sport_car1.turn("Left")
sport_car1.turn("Right")
sport_car1.show_speed()
sport_car1.speed = 110
sport_car1.show_speed()
sport_car1.speed = 120
sport_car1.show_speed()
