class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is", self.cpu, self.ram)


# this will call init method which is basically a constructor
comp1 = Computer('i5', 16)
comp2 = Computer('Ryzen 3', 8)

print(type(comp1))
# 2nd way
comp1.config()
comp2.config()
