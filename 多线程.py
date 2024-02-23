# multithreading
from time import sleep
from threading import *
class Hello(Thread):
    def run(selfs):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(selfs):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()

t2 = Hi()
# Main threading
# t1.run()
# t2.run()
t1.start()
# 两者存在间隙 以防碰撞
sleep(0.2)
t2.start()

t1.join()
t2.join()

# 在join运行完后才执行
print("Bye")