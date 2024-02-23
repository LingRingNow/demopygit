from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = array([1,2,3,4,5])

arr3 = arr1 + arr2

# print(max(arr3))

# print(concatenate([arr1,arr2]))

# arr2 = arr1.view()
arr2 = arr1.copy()

arr1[1] = 7

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
