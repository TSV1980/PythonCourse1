"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import datetime
import time


class TrafficLight:
    """Класс светофор"""

    __its_color__ = "Green"
    """Его текущий цвет"""

    __work__ = False
    '''Светофор работает'''

    def __init__(self) -> None:
        pass

    def running(self):
        '''Запустить светофор'''
        self.__work__ = True
        print(f'Traffic Light is ON')
        while self.__work__:
            # print(self.__its_color__)
            if self.__its_color__ == "Green":
                get_current_light(self.__its_color__)
                time.sleep(5)
                self.__its_color__ = "Red"
            if self.__its_color__ == "Red":
                get_current_light(self.__its_color__)
                time.sleep(7)
                self.__its_color__ = "Yellow"
            if self.__its_color__ == "Yellow":
                get_current_light(self.__its_color__)
                time.sleep(2)
                self.__its_color__ = "Green"

    def switch_off(self):
        '''Выключить светофор'''
        self.__work__ = False
        print(f'Traffic Light is OFF')


def get_current_light(color):
    print(f'Time =  {datetime.datetime.now().strftime("%H:%M:%S")}. Color = {color}')


tr_light1 = TrafficLight()
tr_light1.running()
