def div(a, b):
    return a / b


# here we want to have numerator greate the denomonator before division but without swappingthem inside method

def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

div1 = smart_div(div)
print(div1(2, 4))
