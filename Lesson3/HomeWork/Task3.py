# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов

def my_func3(var1, var2, var3):
    return sum((var1, var2, var3))-min(var1, var2, var3)


nums = input('Введите 3 числа через пробел: ').split()
if (len(nums) == 3):
    print(f'Результат функции: {my_func3(int(nums[0]),int(nums[1]),int(nums[2]))}')
else:
    print('Ошибка ввода!')
