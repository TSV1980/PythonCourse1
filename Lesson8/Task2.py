'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class ZeroDivisionError(Exception):
    def __init__(self, text):
        self.txt = text
        
    def __str__(self):
        return f'User Exception: {self.txt}'
            
    
b = float(input('Введите делимое - b = '))
c = float(input('Введите делитель - с =  '))

try:
    if (c == 0):
        raise ZeroDivisionError('Выполняется деление на ноль')
    res  = b / c
    print(f'Результат деления = {res}')    
except ZeroDivisionError as er:
    print(er)