# 多态 Polymorphism

# duck Typing
# class Duck:
#     def __init__(self, name):
#         self.name = name
#     def duck_walk(self):
#         # print("duck {} walk".format(self.name))
#         # print("duck %s walk" % self.name)
#         print(f"duck {self.name} walk")
#
#     def duck_sound(self):
#         print("duck {} sound".format(self.name))
# class Quanjude:
#
#     @staticmethod
#     def cook(duck):
#         print("check duck")
#         duck.duck_walk()
#         duck.duck_sound()
#         print("check out")
#
# d1 = Duck("d1")
#
# d2= Duck("d2")
#
# Quanjude.cook(d1)
# Quanjude.cook(d2)


# Operator Overloading
# a = 1
# b = 5
# x = int.__add__(a, b)
# print(x)


# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     # 两个实例属性m1， m2相加并返回该实例
#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         return Student(m1, m2)
#
#     def __gt__(self, other):
#         m1 = self.m1 + self.m2
#         m2 = other.m1 + other.m2
#         if m1 > m2:
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         # return self.m1, self.m2,
#         return f"{self.m1} ,{self.m2}"
#         # return "%s, %s" % (self.m1, self.m2)
#         # return "{}, {}".format(str(self.m1), str(self.m2))
#
# s1 = Student(23, 44)
#
# s2 = Student(33, 52)
#
# s3 = Student.__add__(s1, s2)
#
# print(Student.__gt__(s2, s1))
# print(s3.m1)
#
# a = 9
# print(a.__str__())
# print(s1.__str__())

# Method Overloading
# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def sum(self, a=None, b=None, c=None):
#         if a is None and b is None and c is None:
#             return None
#         elif b is None and c is None:
#             return a
#         elif c is None:
#             return b + a
#         return a + b + c
#
#
# s = Student(89, 23)
#
# print(s.sum(2,2))



# Method Overrrding

class A:
    def show(self):
        print("in A Show")

class B(A):
    def show(self):
        print("in B Show")

a1 = B()

a1.show()
