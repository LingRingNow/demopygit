# list = [1,2,3,4,5,6,7,8,9]
#
#
# def count(lst):
#     even = 0
#     odd = 0
#     for i in lst:
#         if i%2 ==0:
#             odd+=1
#         else:
#             even+=1
#     return even,odd
#
# even,odd = count(list)
# print(even,odd)
list =[]

userLength = int(input("Enter the length of users "))

for i in range(userLength):
    char = input("Enter the user name")
    list.append(char)

def usernameSearch(lst):
    oversizeNum = 0
    for i in lst:
        if len(i) > 5:
            oversizeNum += 1
    return oversizeNum

print(usernameSearch(list))

