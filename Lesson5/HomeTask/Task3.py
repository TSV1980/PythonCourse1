# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:

# Иванов 23543.12
# Петров 13749.32

from numpy import append

f_name = 'text_3.txt'

fio_with_big_salary = []
sum_salary = 0

strings_arr = open(f_name,'r', encoding='utf-8').read().split('\n')
for line in strings_arr:
        words = [el for el in line.split() if len(el) >= 2]
        try:
            fio = words[0]
            salary = float(words[1])
        except Exception as ex:
            print(f'Exception = {ex}')
        if (salary < 20000):
            fio_with_big_salary.append(fio)
        sum_salary += salary;
        

print(f'Сотрудники с ЗП меньше 20тр: {fio_with_big_salary}')
print(f'Средняя ЗП сотрудников: {sum_salary/len(strings_arr)}')
