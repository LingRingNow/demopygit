class Car:
    # 静态属性
    # 类命名空间
    wheels = 4

    # 实例方法
    def __init__(self):
        # 实例命名空间
        self.make = 'BMW'
        self.mil = 10

    def avg(self):
        return self.make, self.mil, self

    def get_c1(self):
        return self.make

    def set_c1(self, avg):
        self.make = avg

    #类方法
    @classmethod
    def getWheels(cls):
        return cls.wheels

    #   静态方法
    @staticmethod
    def info():
        print("static")


c1 = Car()

c2 = Car()

result = c1.avg()

print(result)

print(Car.getWheels())
Car.info()