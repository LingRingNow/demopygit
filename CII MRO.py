class A:
    def __init__(self):
        print("__init__ A")

    def feature1(self):
        print("Feature1 workiing A")

    def feature2(self):
        print("Feature2 workiing")


# class B(A):
class B:
    def __init__(self):
        # 超类调用
        super().__init__()
        print("__init__ B")

    def feature1(self):
        print("Feature3 workiing")

    def feature4(self):
        print("Feature4 workiing")

# class C(B,A):
class C(A,B):
    def __init__(self):
        super().__init__()
        print("__init__ C")

    def fear(self):
        super().feature2()

a1 =C()

a1.fear()