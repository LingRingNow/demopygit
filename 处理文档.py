# File handling
# 储存数据在程序运行完后
"""
Created on
@Author: <NAME>


"""
f = open("Data/myData.txt", encoding="utf-8")

print(f.readline(1),end="#")
print(f.readline(2),end="#")

#  w代表
f1 = open("Data/writeDemo.txt", "w")
f1.write("new example")
# open for writing, truncating the file first
# f1.write("over write")

for data in f:
    f1.write(data)

f_img = open('Img/1-full.jpg', 'rb')

f_wImg = open('Img/newPic.jpg', 'wb')

for data in f_img:
    f_wImg.write(data)
