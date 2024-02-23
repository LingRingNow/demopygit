from array import *
values = array('i', [2,3,4,5,6])

newArray = array(values.typecode, (a*a for a in values))

for i in newArray:
    print(i)
