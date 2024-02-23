# def add(a,b):
#     c = a + b
#     print(c)
#
# add(1,4)

# def person(name, age=18):
#     print(name)
#     print(age-5)
# # 报错顺序错误
# # person(2,"John")
#
# # person(age=20, name='John')
#
# person("navin")

def sum(a,*b):
    # print(a)
    # print(b)
    c = a
    for i in b:
        c += i
        
    print(c)
    # c=a+b
    # print(c)

sum(2,4,1,4)