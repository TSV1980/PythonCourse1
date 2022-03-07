''' 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30} '''


f_name_read = 'text_6.txt'
f_name_write = 'text_6_new.txt'
res_dict = {}

with open(f_name_read, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
        for el in lines:
            words = el.split(':')
            if (len(words) == 2):
                # words[0] - название предмета
                # hours_education[1] - информация о занятиях
                hours_education = words[1].split('(')
                sum_hours = 0
                for i, el in enumerate( hours_education):
                    if (i < len(hours_education)-1):
                        sum_hours += int(str(el).replace('(','').replace(')','').replace('л','').replace('пр','').replace('лаб','').replace('-','').replace('\n',''))
                res_dict.update({f'{words[0]}':sum_hours})    


print(res_dict)


with open(f_name_write, 'w', encoding='utf-8') as fw:
    for key,val in res_dict.items():
        fw.write(f'Name:{key}. Hours = {val} \n')

                
