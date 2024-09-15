#Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.

# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчёте на одного сотрудника.

company_revenue = int(input('Введите выручку фирмы:'))
company_costs = int(input('Введите издержки фирмы:'))

delta = company_revenue - company_costs

if (delta > 0):
    print('Фирма работает с прибылью.')
    numpeople = int(input('Введите количество сотрудников в фирме:'))
    print(f'Прибыль фирмы в расчете на одного сотрудника равна {delta / numpeople :.2f}')
else:
    print('Фирма работае с издержками.')

