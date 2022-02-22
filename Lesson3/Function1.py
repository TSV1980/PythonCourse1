import FunctionLib as FL

def my_sum(arg1,arg2):
    res = arg1 + arg2
    return arg1 + arg2

def my_pass():
    pass

def my_f1(s1,s2):
    sub = s1 + s2
    print(f'res ={sub}')

def my_f2(var1,var2,var3=10):
    addR = var1 + var2 + var3
    print(f'RES F2 = {addR}')

def my_f3(var1, var2, var3 =55):
    addRRR = var1 + var2 + var3
    return  addRRR, var2,' OK'

print(f'RESFL = {FL.MyFx1(1,2,3,4,5,6,a=1,b=2,c=3)}')


print(f'ADDR3 = {my_f3(5,55,10)}')

print(f"Результат функции {my_sum(45,54)}")

my_pass()

my_f1(63,45)

my_f2(45,56,67)
my_f2(var2=45,var1=23)
my_f2(var1=1,var2=2,var3=3)


mmm = [3,1]
FL.MyFx2(mmm)
print(f'mmm = {mmm}')

print(FL.MyFx3(5,10,{2:4}))
print(FL.MyFx3(5,10))
print(FL.MyFx3(6,24))
print(FL.MyFx4(5,5))


a = ['F1','SEC2','TTT3','fds5','ddfsg4']
a.sort(key= lambda pos : pos[0])
a.sort(key= lambda pos : pos[-1])
print(a)

print(chr(45))
print(ord('A'))




