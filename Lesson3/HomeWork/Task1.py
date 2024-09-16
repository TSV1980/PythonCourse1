# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#  Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide_nums(val1, val2=1):
    """Функция деления двух чисел.
    Именованные параметры:
    val1 -- делимое (по умолчанию 0.0)
    val2 -- делитель (по умолчанию 1.0)
    """
    if (val2 == 0):
        print('Ошибка! Деление на 0.')
        return val1
    else:
        return  val1/val2

help(divide_nums)

print("Программа деления двух чисел.")
num1 = int(input('Введите первое числа - делимое:'))
num2 = int(input('Введите второе число - делитель:'))

print(f'Результат операции = {divide_nums(val1=num1,val2=num2):0.2f}')
