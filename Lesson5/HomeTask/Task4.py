# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. 
# Новый блок строк должен записываться в новый текстовый файл.

translate = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}

f_name_read = 'text_4.txt'
f_name_write = 'text_4_new.txt'

with open(f_name_read, 'r', encoding='utf-8') as fr:
    with open(f_name_write, 'w', encoding='utf-8') as fw:
        lines = fr.readlines()
        for el in lines:
            words = el.split()
            if (len(words) == 3):
                newstr = translate[words[0]] + ' ' + words[1] + ' ' + words[2] + '\n'
                fw.write(newstr) 
                           