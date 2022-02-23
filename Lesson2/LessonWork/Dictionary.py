
print(dict(a=1,b=2))

my_dict = dict(age = 42, name = 'Sergey', sex = 'M', city = "Moscow")

print(my_dict)
print(my_dict['age'])
print(my_dict['name'])

print(my_dict.keys())

for key,value in my_dict.items():
    print(key,value)

print('*' * 100)
print(type(my_dict))
print(True if  my_dict is set else False)