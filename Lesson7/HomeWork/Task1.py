"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    """Класс МАТРИЦА"""
    
    def __init__(self,param):
        self.param = param
        for line in self.param[:-1]:
            if not len(line) == len(self.param[self.param.index(line)+1]):
                raise ValueError('Строки в матрице не одинаковой размерности')
        
    #def __str__(self):
    #    res = ""
    #    for line in self.param:
    #        res += str(line).replace(',',' ').replace('[','|').replace(']','|') + '\n'
    #    return res
    
    def __str__(self):
        '''Переопределение метода преобразования в строку'''
        return '\n'.join('   '.join(str(num) for num in line) for line in self.param)   
   
    def __add__(self, other):
        '''Переопределение метода сложения матрицы'''
        if not len(self.param) == len(other.param):
            raise ValueError('Размерности матриц не совпадают')
        item = []
        for row in range(len(self.param)):
            item.append([])
            for col in range(len(self.param[row])):
                item[row].append(self.param[row][col] + other.param[row][col]) 
        return Matrix(item)
    
        
    def __sub__(self, other):
        '''Переопределение метода вычитания матрицы'''
        if not len(self.param) == len(other.param):
            raise ValueError('Размерности матриц не совпадают')
        item = []
        for row in range(len(self.param)):
            item.append([])
            for col in range(len(self.param[row])):
                item[row].append(self.param[row][col] - other.param[row][col]) 
        return Matrix(item)
    
    #def __add__(self, other):
    #    if not len(self.param) == len(other.param):
    #        raise ValueError('Размерности матриц не совпадают')
    #    item = [[int(self.param[line][num] + other.param[line][num]) for num in range(len(self.param[line]))] for line in range(len(self.param))]
    #    return Matrix(item)
    
 
m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = Matrix([[1,2,3],[1,1,1],[2,2,2]])
print('Матрица М1:')
print(m1)
print('Матрица М2:')
print(m2)
print('\n')
print('Матрица М1+M2:')
print(m1 + m2)
print('\n')
print('Матрица М1-M2:')
print(m1 - m2)
print('\n')

'''
m3 = Matrix([[1,2,3],[4,6],[7,8,9]])
m4 = Matrix([[1,2,3],[1,1,1],[2,2]])
print('Матрица М3:')
print(m3)
print('Матрица М4:')
print(m4)
print('\n')
print('Матрица М3+M4:')
print(m3 + m4)
print('\n')
'''
