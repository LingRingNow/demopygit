l = [8,3,65,34,77,11,2,46,87,4]


def sort(list):
    for i in range(len(list)):
           minpos = i
           for j in range(i + 1, len(list)):
               if list[j] < list[minpos]:
                   minpos = j
           temp = list[i]
           list[i] = list[minpos]
           list[minpos] = temp
    return list

sl = sort(l)

print(sl)

