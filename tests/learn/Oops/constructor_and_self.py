class Computer:
    def __init__(self, name , age):
        self.name = name
        self.age = age


c1 = Computer('dipendra',33)
print(id(c1))
c2 = Computer('Sonali', 30)
print(id(c2))


print(c1.name)
print(c2.name)
