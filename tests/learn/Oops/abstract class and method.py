# ABC - Abstract base classes
from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):  # declaration -- abstarct method
        pass


class Laptop(Computer):
    def process(self):
        print("Laptop process")

# and class which have least 1 abstract method is abstract classes
# We can;t create object of abstract classed

# com = Computer()
# com.process()  # this will give error


lap1 = Laptop()
lap1.process() #this will also give erro if we don;t have process method in other callss



#use of abstract method and class - Only when we design application in oops way.
#if you create a abtsratct class with abstract method then other calss who extend this class will have to define those methods.