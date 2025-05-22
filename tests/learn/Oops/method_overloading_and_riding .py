# two methdo wiyj same name and different number of parm is method overlading
# not supported in python

# method overriding
class A:
    def show(self):
        print('in A show')


class B(A):
    def show(self):  # this is method overriding
        print("in B show")


obj1 = A()
obj1.show()

obj2 = B()
obj2.show()
