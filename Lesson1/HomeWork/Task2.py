#Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

usersec = int(input('Введите время в секундах:'))

calchour = usersec // 3600
print(f"Количество часов {calchour:02d}")

calminutes = (usersec - (calchour * 3600)) // 60
print(f"Количество минут {calminutes:02d}")

calsecs = usersec - (calchour * 3600) - (calminutes * 60)
print(f"Количество секунд {calsecs:02d}")

print(f'Указанные минуты в формате чч:мм:сс - {calchour:02d}:{calminutes:02d}:{calsecs:02d}"')