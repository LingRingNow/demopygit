nums = [1,2]
#
# print(nums)
# #
# # for i in nums:
# #     print(i)
#
# it = iter(nums)
#
# print(next(it))
# print(it.__next__())

# 创建一个迭代器
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = TopTen()

print(next(values))

for i in values:
    print(i)