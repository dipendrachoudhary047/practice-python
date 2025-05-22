def greet():
    print("Hello, world!")
    print("Goodbye, world!")


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def add_sub(a, b):
    c = a + b
    d = a - b
    return c, d


# greet()
value1, value2 = add_sub(5, 2)
print(value1, value2)
