l = [8,3,65,34,77,11,2,46,87,4]

def bubbleSort(list):
    # 升序
    # for i in range(0, len(list)-1):
    #     for j in range(i,len(list)-1):
    # 降序
    for i in range(len(list)-1 , 0 , -1):
        for j in range(i):
#             swap操作
            if list[i] > list[j]:
                temp =  list[i]
                list[i] = list[j]
                list[j] = temp
    return list
sortList = bubbleSort(l)
print(sortList)