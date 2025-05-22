# def square(x):
#     return x * x
#
#
# result = square(5)
# print(result)

'''
f = lambda a, b: a + b
result = f(2, 8)
print(result)
'''

# Using lambda function in other function
from functools import reduce


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


nums = [1, 21, 33, 4, 32, 6, 8, 8, 9]

# filter - to filter out
evens = list(filter(lambda i: i % 2 == 0, nums))
print(evens)

# map - to change values
doubles = list(map(lambda j: j * 2, evens))
print(doubles)

# reduce - to reduce values
sum = reduce(lambda a, b: a + b, doubles)
print(sum)
