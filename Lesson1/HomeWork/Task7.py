#Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

first_day_km = int(input('Сколько км пробежал спортсмен в первый день?:'))
last_day_km = int(input('Сколько км должен пробежать спортсмен как результат подготовки?:'))

num_of_days = 1;

while first_day_km < last_day_km:
    first_day_km *= 1.1 #увеличиваем  реузльтат на 10%
    num_of_days += 1    #увеличиваем  количество дней
    print(f'На {num_of_days} день спортсмен пробежит {first_day_km:0.1f}')

print(f'Результата спортсмен достигнет на {num_of_days:00d}')


