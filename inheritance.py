class A:
    def feature1(self):
        print("Feature1 workiing")

    def feature2(self):
        print("Feature2 workiing")


class B(A):
    def feature3(self):
        print("Feature3 workiing")

    def feature4(self):
        print("Feature4 workiing")

class C(B):
    def feature5(self):
        print("Feature5 workiing")

a1 = A()

a1.feature1()

b1 = B()

c1 = C()

c1.feature1()