#Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

print(f'Параметры вызова программы: {argv}')

if (len(argv) >= 4):
    try:
        print(f'Заработная плата сотрудника = {(int(argv[1]) * int(argv[2]) + int(argv[3]))}')
    except Exception as e:
        print(f'Ошибка: {e}')

else:
    print('Недостаточно параметров.')
