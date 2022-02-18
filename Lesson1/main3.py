num = int(input('Введите число от 0 до 9:'))

while num <= 10:
    print(num)
    num += 1


i = 0
while True:
    i += 1
    if i >= 10:
        break # выходим
    if i % 2 == 0:
        continue # возврат к while

