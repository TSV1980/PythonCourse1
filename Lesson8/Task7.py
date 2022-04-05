'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение
созданных экземпляров. Проверьте корректность полученного результата.
'''


class ComplexNum:
    
    def __init__(self,a , b):
        self.a = a
        self.b = b
        
    def __str__(self):
        if self.b >= 0:
            return f'{self.a}+{self.b}j'
        else:
            return f'{self.a}{self.b}j'
    
    def __add__(self, other):
        res = ComplexNum(0,0)
        res.a = self.a + other.a
        res.b = self.b + other.b
        return res

    def __sub__(self, other):
        res = ComplexNum(0,0)
        res.a = self.a - other.a
        res.b = self.b - other.b
        return res    
    
    def __mul__(self, other):
        res = ComplexNum(0,0)
        res.a = self.a * other.a - self.b * other.b
        res.b = self.a * other.b + self.b * other.a
        return res    
        
    def __truediv__(self, other):
        if (other.a * other.a  + other.b * other.b != 0):
            res = ComplexNum(0,0)
            res.a = (self.a * other.a + self.b * other.b) / (other.a * other.a  + other.b * other.b)
            res.b = (self.b * other.a - self.a * other.b) / (other.a * other.a  + other.b * other.b)
            return res
        else:
            print('Деление на ноль невозможно')
            return None
            
    
print('*' * 100)
print('Первый вариант проверки')
    
c1 = ComplexNum(2,3)
c2 = ComplexNum(5,5)

print(f'c1 = {c1}')
print(f'c2 = {c2}')

print(f' c1 + c2 = {c1 + c2}')
print(f' c1 - c2 = {c1 - c2}')
print(f' c1 * c2 = {c1 * c2}')
print(f' c1 / c2 = {c1 / c2}')

print('Проверка работы класса на встроенной библиотеке')
ax = 2 + 3j
bx = 5 + 5j

print(ax + bx)
print(ax - bx)
print(ax * bx)
print(ax / bx)

print('*' * 100)
print('Второй вариант проверки')

c3 = ComplexNum(2,-3)
c4 = ComplexNum(-5,5)

print(f'c3 = {c3}')
print(f'c4 = {c4}')

print(f' c3 + c4 = {c3 + c4}')
print(f' c3 - c4 = {c3 - c4}')
print(f' c3 * c4 = {c3 * c4}')
print(f' c3 / c4 = {c3 / c4}')

print('Проверка работы класса на встроенной библиотеке')
ax = 2 - 3j
bx = -5 + 5j

print(ax + bx)
print(ax - bx)
print(ax * bx)
print(ax / bx)

print('*' * 100)
    
    