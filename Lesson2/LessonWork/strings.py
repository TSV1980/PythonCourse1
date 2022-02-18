my_str = "простая строка"
print(my_str)
print(type(my_str))

print("Hi " * 10)

s1 = 'abra'
s2 = 'kadabra'
print(s1 + s2)

s = 'abrakadabra'
print(s[4:7])
print(s[3:-3])
print(s[:5])
print(s[3:])
print(s[:])
print(s[::-1])
print(s[1:7:2])

string2 = "abrakadbra"
str_reverse = string2[::-1]
print(str_reverse)


string2 = "abrakadabra"
str_reverse = ''
symbols = list(string2)
for el in range(len(string2) // 2):
    tmp = symbols[el]
symbols[el] = symbols[len(string2) - el - 1]
symbols[len(string2) - el - 1] = tmp
str_reverse = ''.join(symbols)
print(str_reverse)

print(len(string2))
list1 = 'sfd fgfd sdfd'.split(' ')
print(list1)
print(''.join(list1))
print('***'.join(list1))
print('---'.join(list1))

print(string2.upper())
print(string2.lower())

STR3 = 'Привет Мой Милый Друг'
print(STR3.istitle())
print(STR3.lower())
print(STR3.lower().title())
print(STR3.lower().capitalize())
print(STR3.lower().capitalize().swapcase())
print(STR3.lower().capitalize().swapcase().swapcase().startswith('При'))



print('ПРОСТАЯ СТРОКА'.isupper())
print('простая строка'.isupper())

print('ПРОСТАЯ СТРОКА'.islower())
print('простая строка'.islower())


print(ord('b'))
print(chr(98))

print('рарара'.count('ра'))

print('рарарара'.index('ра'))


print('рарарара'.find('ра'))

print('рарарара'.replace('pa','hi'))

STR5 = 'Hi my dear'
dir(STR5)
