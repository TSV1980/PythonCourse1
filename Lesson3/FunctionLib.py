
#def Calculate(var1,var2,action):
#    if (action == '+'):

def MyFx1(*args,**kwargs):
    return sum(args) + sum(kwargs.values())

def MyFx2(m):
    m.append(1)
    return  m

def MyFx3(key,value,a=None):
    if a is None:
        a = {}
    a[key] = value
    return a

MyFx4 = lambda  a1,a2 : a1 + a2


def my_path_f():
    """Возвращает путь к файлу"""
    global mypath
    mypath  = 'file.txt'
    return  mypath

help(my_path_f)
print(my_path_f())
print(mypath)
