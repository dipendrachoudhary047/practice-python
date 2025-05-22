def test_normal_variable():
    x = 3
    print(x)
    name = ("dipendra")
    print(name)
    print(name[1])
    print(name[-1])
    print(name[1:4])
    print(name[:5])
    print(name[2:])
    name = "naveen's"
    print(name)
    print('\n')
    name1 = 'naveen\'s "laptop"'
    print(name1)
    directory = ('c:\docs\naveen')  # this creates issue as \n gives new line
    print(directory)
    directory1 = (r'c:\docs\naveen')
    print(directory1)


def test_math_variables():
    var1 = 2 + 3
    print(var1)
    var2 = 10 / 3  # this will give fload value
    print(var2)
    var3 = 10 // 3  # this will give only integer value
    print(var3)
    var4 = 10 % 3  # this will give modulus
    print(var4)
    var5 = 10 ** 3
    print(var5)


def test_mutable_string():
    str1 = 'dipendra'
    print(str1)
    str1[
        1] = 'ts'  # this will give error as string is immutable mesn assignment can't be changed
    print(str1)



def test_string_methods():
    str1 = '    dipendra choudha ry     '
    print(str1.strip()) # delete space from end and start
    print(str1.count('a')) #count occourance of 'a'
    print(str1.title())
    print(str1.upper())
    print(str1.lower())
    print(str1.replace(' ', ''))
    print(str1.split(' '))
    str1.capitalize()
    print(str1.find('d'))
    print(str1.index('d'))
    print(set(str1))


# #None
# from typing import Tuple
#
# Numeric
#     int
#     float
#     complex
#     bool
#
# List
# Tuple
# set
# range
# dictionary

def test_range():
    range(10)
    print(list(range(10)))

    range(2, 10, 2)
    print(list(range(2, 10, 2)))








