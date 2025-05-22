from pyee import cls


class Student():
    school = "DPS"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    @classmethod
    def get_school_name(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class ")


s1 = Student(10, 20, 30)
s2 = Student(40, 50, 60)

print(s1.m1, s1.m2, s1.m3, Student.school)
print(s2.m1, s2.m2, s2.m3, Student.school)

print(s1.average())
print(s2.average())

print(s1.get_m1())
print(s2.get_m1())

print(Student.get_school_name())

s1.info()
Student.info()
