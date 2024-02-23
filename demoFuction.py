def update(lst):

    print(lst)
    print(id(lst))

    lst[1] = 3
    print(lst)
    print(id(lst))

list = [12, 34 ,55]
update(list)
print(list)
print(id(list))
