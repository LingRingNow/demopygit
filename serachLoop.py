pos = -1
def searchFor(list, n):
    # i = 0
    # while i <len(list):
    #     if list[i] == n:
    #         globals()['pos'] = i
    #         return i
    #     i += 1

    for i in range(0, len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False
l = [1, 3, 5, 78, 9]

if searchFor(l, 9):
    print("Found", pos)
else:
    print("Not found")
