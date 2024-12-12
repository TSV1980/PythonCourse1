''' 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со 
средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста. '''

import json

f_name_read = 'text_7.txt'
f_name_write = 'text_7_new.json'
res_dict_firms = {}
profits = []
res_list = []

with open(f_name_read, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
        for el in lines:
            words = el.split()
            if (len(words) == 4):
                # words[0] - название 
                # words[1] - форма собственности
                # words[2] - выручка
                # words[3] - издержки
                delta = int(words[2]) - int(words[3])
                res_dict_firms.update({words[0] : delta})
                if (delta > 0):
                    profits.append(delta)

res_list.append(res_dict_firms)
res_list.append({'average_profit':sum(profits)/len(profits)})

print(res_list)

with open(f_name_write, "w", encoding='utf-8') as write_f:
    json.dump(res_list, write_f)