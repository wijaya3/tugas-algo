import array as arr

array_1 = arr.array('i',(90,80,70,60))
print(array_1)

print(array_1('i'))

array_1.append(100)
print(array_1)

array_1[3] = 10
print(array_1)