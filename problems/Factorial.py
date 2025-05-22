n = 4

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

value = factorial(n)
print(value)