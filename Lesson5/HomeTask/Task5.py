# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

nums = [342, 34, 67, 435, 12, 876, 65, 345, 324, 86, 435, 567, 76, 834]
#nums = [1, 2, 3, 4]

f_name_write = 'text_5_new.txt'
with open(f_name_write, 'w', encoding='utf-8') as fw:
    for j in nums:
        fw.write(str(j) + ' ')

with open(f_name_write, 'r', encoding='utf-8') as fr:
    read_nums = map(int, fr.read().rsplit())
     
print(f'Сумма чисел в файле:{sum(read_nums)}')
