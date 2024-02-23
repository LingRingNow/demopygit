class Student():

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.ram = 8
            self.cpu = "i8"

s1 = Student('')
s2= Student('<NAME>')