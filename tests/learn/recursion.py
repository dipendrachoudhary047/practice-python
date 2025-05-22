# function calling itself is recursion

i = 0
def greet():
    global i
    i = i+1
    print("Hello", i)
    greet()


greet()

# default limit for printing is 1000
