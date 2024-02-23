from numpy import *

arr1 = array([
    [1, 2, 3, 4, 2, 6],
    [4, 5, 6, 4, 7 ,8]
])
arr2 = arr1.flatten()
#转化为一个大数组包含两个二维数组， 每个二维数组有两个一维数组，每个数组有3个元素
# arr3 = arr2.reshape(2, 2, 3)

# print(arr3)

# print(arr1.size)
# 转化为矩阵
# m = matrix(arr1)

ms = matrix('1 2 3 6 ; 6 5 2 5; 3 4 5 6; 2 4 6 0')

# print(diagonal(ms))
# print(ms.max())
# print(ms)

# 矩阵相乘
m1 = matrix('1 2 3 ; 6 5 2; 1 6 7')
m2 = matrix('1 2 3 ; 6 8 2; 2 6 7')

m3= m1 * m2
print(m3)