'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''



class MyDate:
    
    my_day = 1
    
    my_year = 2022
    
    my_mounth = 1
    
    def __init__(self,strdate) -> None:
        self.strdate = strdate
    
    def __str__(self):
        return f'Заданная дата:{self.my_day}-{self.my_mounth}-{self.my_year}'
    
    @classmethod
    def get_date_info(cls, strdate):
        '''strdate формата «день-месяц-год»'''
        params = str(strdate).split('-')
        if len(params)  == 3:
            cls.my_day = int(params[0])
            cls.my_mounth = int(params[1])
            cls.my_year = int(params[2])
        return cls(strdate)
    
    @staticmethod
    def validate_date(self):
        assert self.my_day >= 1 and  self.my_day <= 31 , 'День должен быть от 1 числа до 31 числа'
        assert self.my_mounth >= 1 and  self.my_mounth <= 12 , 'Месяц должен быть от 1 числа до 12'
        assert self.my_year >= 1900 and  self.my_year <= 2100 , 'Год должен быть от 1900 числа до 2100'
         
    
    

my_date1 = MyDate.get_date_info('02-04-2022')
print(str(my_date1))

MyDate.validate_date(my_date1)


    
    