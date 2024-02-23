# Midinde = (lower + upper) / 2


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binarySearch(list, n):
    l = 0
    h = len(list) - 1
    while l <= h:
        mid = (l + h) // 2
        if list[mid] == n:
            return mid
        elif list[mid] < n:
            l = mid + 1
        else:
            h = mid - 1


r = binarySearch(list, 4)

print(r)
