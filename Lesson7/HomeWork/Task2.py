"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
 реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

class Clothes(ABC):
    '''Абстрактный класс'''
    
    fabric_cnt  = 0
    '''Атрибут класса для подсчета общего количество материала'''
    
    @abstractmethod
    def material_expence(self):
        '''Абстрактный метод'''
        pass

 
class Coat(Clothes):
    '''Клас Пальто'''
    
    def __init__(self,v):
        self.v = v
        Coat.fabric_cnt += self.material_expence
        
    def __str__(self):
        return f'Размер пальто:{self.v}. Расход ткани {self.material_expence}. Общий расход {Coat.fabric_cnt}'
    
    @property
    def material_expence(self):
        '''для пальто (V/6.5 + 0.5)'''
        res = self.v / 6.5 + 0.5;
        return float(f'{res:.01f}')
    
      
class Suite(Clothes):
    '''Клас Костюм'''
        
    def __init__(self,h):
        self.h = h
        Suite.fabric_cnt += self.material_expence
        
    def __str__(self):
        return f'Рост для костюма:{self.h}. Расход ткани {self.material_expence}. Общий расход {Suite.fabric_cnt}'
    
    @property
    def material_expence(self):
        '''для костюма (2*H + 0.3)'''
        res = self.h / 2.0 + 0.3;
        return float(f'{res:.01f}')
    

coat_1 = Coat(48)
print(coat_1)
coat_2 = Coat(52)
print(coat_2)

suit_1 = Suite(176)
print(suit_1)
suit_2 = Suite(180)
print(suit_2)
