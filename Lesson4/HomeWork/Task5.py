# Реализовать формирование списка, используя функцию range() и возможности генератора.
#  В список должны войти чётные числа от 100 до 1000 (включая границы).
#  Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def mul_func(var1,var2):
    return var1 * var2


my_list = [el for el in range(100,1001,2)]
print(f'List:\n{my_list}\nResult list:\n{reduce(mul_func,my_list)}')
