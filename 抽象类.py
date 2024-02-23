# ABC Abstract Base Class
# 抽象类不能被实例化，只能被继承，且子类必须实现抽象方法
# 抽象类就是从一堆对象(类)中抽取相同内容，内容包括数据属性，函数属性
from abc import ABC, abstractmethod
class Computer(ABC):
    # 定义抽象方法无需实现功能
    @abstractmethod
    # 子类必须定义process方法
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("running laptop")

class WhiteBoard(Computer):
    def process(self):
        print("running laptop")

    def write(self):
        print("wr")
class Progranner:
    def work(self, com):
        print("running progranner")
        com.process()

# com = Computer()
com = Laptop()
# com.process()
com2 = WhiteBoard()

prog = Progranner()
prog.work(com2)
