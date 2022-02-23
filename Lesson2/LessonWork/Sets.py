a = {1,2,3,4,1,2,3,0,3,0,6,4,5}
print(type(a))
print(a)
print(6 in a)

b = {4,3,4,6,8,9,4,9,11}
print(b)

c = a.intersection(b)
print(c)

c = a.symmetric_difference(b)
print(c)

c = a - b
print(c)



print(set('gippopotam'))

mysss = {2,3,4.333,False,True,(2,3,4)}
mysss.add('fffgfgf')
print(mysss)


print(mysss.pop())

print(mysss.discard(0))

print(mysss.discard(3))


print(frozenset({2,3,45,6,3,4}))