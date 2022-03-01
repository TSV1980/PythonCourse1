#6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
#   но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
#  Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
#  но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(word):
    if (len(word) >= 2):
        return word[0].upper() + word[1:].lower()

# Test int_func
print(f' Test -int_func- Function. Res = {int_func("house")}')

text = input('Введите строку из слов, разделённых пробелом: ').split()
res_str = ''
for i,word in enumerate(text):
    if (not  str(word).isascii() or not str(word).isalpha() or not str(word).islower()):
        print(f'Слово {word} не удовлетворяет условиям')
    else:
        res_str += ' ' + str(int_func(word))

print(f'Результат = {res_str}')
