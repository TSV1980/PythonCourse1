# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

f_name = 'Task2_File.txt'

strnum = 1
strings_arr = open(f_name,'r', encoding='utf-8').read().split('\n')
for line in strings_arr:
        words = [el for el in line.split() if len(el) >= 2]
        print(f'В строке {strnum} - {len(words)} слова')
        strnum += 1

print(f'В файле {strnum} строк')

