class Car:
    wheels = 4  # class variable Static variable

    def __init__(self):
        self.mil = 10  # instance Variable
        self.com = 'BMW'  # instance Variable


c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
