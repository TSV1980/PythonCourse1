'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе
определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
'''

from abc import abstractmethod

class Office_Equipment:
    
    equipment_cnt = 0
   
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Equipment {self.name}. Price = {self.price}"
    
    @abstractmethod
    def add_nums(self):
        pass
    
    @abstractmethod
    def sub_nums(self):
        pass
    
  
        
class Printer(Office_Equipment):
    
    def __init__(self, name, price,num_of_colors):
        self.__num_of_colors = Printer._validator2(num_of_colors)
        super().__init__(Printer._validator(name), price)
        
    def add_nums(self):
        Printer.equipment_cnt += 1
        
    def sub_nums(self):
        Printer.equipment_cnt -= 1
        
    def set_num_of_colors(self, num_of_colors):
        self.__num_of_colors = num_of_colors
    
    def get_num_of_colors(self):
        return self.__num_of_colors
        
    def __str__(self):
        return f"Equipment Printer With Name {self.name}. Num Of Colors {self.__num_of_colors}. Price = {self.price}"
    
    @staticmethod
    def _validator(name):
        if len(name) < 2:
            raise ValueError("Name is vary short")
        return name
    
    @staticmethod
    def _validator2(num_of_colors):
        if num_of_colors < 0 or num_of_colors > 6:
            raise ValueError("Error in num of colors")
        return num_of_colors
 

class Scanner(Office_Equipment):
    
    def __init__(self, name, price,resolution):
        self.__resolution = resolution
        super().__init__(name, price)
        
    def add_nums(self):
        Scanner.equipment_cnt += 1
        
    def sub_nums(self):
        Scanner.equipment_cnt -= 1        
        
    def set_resolution(self, resolution):
        self.__resolution = resolution
    
    def get_resolution(self):
        return self.__resolution        
        
    def __str__(self):
        return f"Equipment Scanner With Name {self.name}. Resolution {self.__resolution}. Price = {self.price}" 
    
    
class Xerox(Office_Equipment):
    
    def __init__(self, name, price,paper_size):
        self.__paper_size = paper_size
        super().__init__(name, price)
        
    def set_paper_size(self, paper_size):
        self.__paper_size = paper_size

    def add_nums(self):
        Xerox.equipment_cnt += 1
        
    def sub_nums(self):
        Xerox.equipment_cnt -= 1               
    
    def get_paper_size(self):
        return self.__paper_size     
            
    def __str__(self):
        return f"Equipment Xerox With Name {self.name}. Size of paper {self.__paper_size}. Price = {self.price}"     
    
 

class Equipment_Warehouse:
     
    __all_office_equipment  = list()
     
    def __init__(self, name):
         self.name = name
         
    def __str__(self):
        for eq in self.__all_office_equipment:
            print(eq)
        return '\n'         
         
    def add_new_equipment(self, *equipment):
            for eq in equipment:
                self.__all_office_equipment.append(eq) 
                eq.add_nums()
                
    def remove_equipment(self, name):
        for eq in self.__all_office_equipment:
            if eq.name == name:
                print(f'Отгружаем товар {str(eq)}')
                self.__all_office_equipment.remove(eq) 
                eq.sub_nums()
                
    def print_cnt(self):
        dict_num = {}
        for eq in self.__all_office_equipment:
            if isinstance(eq, Printer):
                dict_num.update({'Printer': eq.equipment_cnt})
            if isinstance(eq, Scanner):
                dict_num.update({'Scanner': eq.equipment_cnt})
            if isinstance(eq, Xerox):
                dict_num.update({'Xerox': eq.equipment_cnt})
        for key,value in dict_num.items():
            print(f'Вид товара: {key}. Количество на складе: {value}')
        return '\n' 
        
    
         
# Проверка работы программы
warehouse_1 = Equipment_Warehouse('Основной склад')

printer_1 = Printer('Samsung', 1500, 3)
printer_1.set_num_of_colors(5)
print(f'Количество цветов у принтера Samsung = {printer_1.get_num_of_colors()}')
printer_2 = Printer('HP',2000,5)
warehouse_1.add_new_equipment(printer_1,printer_2)   

scanner_1 = Scanner("Canon", 2000, 1200)
scanner_2 = Scanner("Epson", 1000, 600)
warehouse_1.add_new_equipment(scanner_1,scanner_2)   

xerox_1 = Xerox("X1", 1234, 'A4')
xerox_2 = Xerox("X2", 3421, 'A3')
xerox_3 = Xerox("X3", 5434, 'A1')
warehouse_1.add_new_equipment(xerox_1,xerox_2,xerox_3)   

print(warehouse_1)
warehouse_1.print_cnt()

print("*"*100)

warehouse_1.remove_equipment('HP')
warehouse_1.remove_equipment('Epson')
warehouse_1.remove_equipment('X3')
print('')
print(warehouse_1)
warehouse_1.print_cnt()
print("*"*100)

# ********************************************************************************
         
