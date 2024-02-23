class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print("init", cpu, ram)
        print(self)

    def config(self):
        print('Attribute',self.cpu,self.ram)


c1 = Computer("intel", 19)
c2 = Computer("amd", 12)

c1.config()