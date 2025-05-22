class A:
    def feature1(self):
        print("feature1 working")

    def feature2(self):
        print("feature2 working")


class B(A):
    def feature3(self):
        print("feature3 working")

    def feature4(self):
        print("feature4 working")


# can also be write like class C(A,B): in case b in already not inherited
class C(B):
    def feature5(self):
        print("feature5 working")


'''
A is superclass
B is subclass
'''

a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature1()  # calling method of Parent class A

c1 = C()
c1.feature4()
c1.feature1()
c1.feature5()
