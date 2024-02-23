def factorial(n):
    latestNum = 1
    for i in range(1, n):
        print(latestNum, 'x', i+1, '=')
        latestNum = latestNum * (i+1)
    return latestNum
# def factorial(n):
#     latestNum = 1
#     for i in range(1, n+1):
#         print(latestNum, 'x', i, '=')
#         latestNum = latestNum * i
#     return latestNum
#
# print(factorial(4))


print(factorial(4))