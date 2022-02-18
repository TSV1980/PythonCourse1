from copy import  deepcopy

newlist = [1,3,5,7]
print(type(newlist))

newlist2 = [2,5.34,False, 'dsfds', (4,2) ,[1,3,4]]
print(newlist2[0:1])
print(newlist2.copy())

newDCopy = deepcopy(newlist2)

print(newDCopy)

newDCopy[0] = 5.673

print(newDCopy)
newDCopy.append(['a','b','c'])

newDCopy.insert(2,6.34543)
print(newDCopy)

print(f'Length of STR = {len(newDCopy)}')

print(newDCopy.pop())

print(newDCopy)

print(newDCopy.remove(False))

print(newDCopy)
print(newDCopy.pop(2))
print(newDCopy)

newDCopy *= 2
print(newDCopy)

newDCopy += 'gdsfasdsfweqertre'
print(newDCopy)

newLST = [3,6,5,2,0]
print(newLST.sort())
