"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    """ Канцелярская принадлежность  """
    
    title = 0
    """ Название    """ 
    
    def __init__(self, title):
        self.title = title
        print(f' У нас новая канцелярская принадлежность - {self.title}')
        
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
        
    def draw(self):
        print(f'{self.title}. Ручка рисует тонкие четкие линии. И их сложно стирать.')


class Pencil(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
        
    def draw(self):
        print(f'{self.title}. Карандаш рисует тонкие четкие линии. И их МОЖНО стирать.')


class Handle(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
        
    def draw(self):
        print(f'{self.title}. Маркером обычно пишут на досках на презентациях.')
        
        
pen_1 = Pen("Ручка Синяя")
pen_1.draw()
print('\r')

pencil_1 = Pencil("Карандаш мягкий")
pencil_1.draw()
print('\r')

handle_1 = Handle("Маркер синий толстый")
handle_1.draw()
print('\r')