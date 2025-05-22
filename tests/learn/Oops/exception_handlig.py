# compile time - #syntax error
# logical error -
# runtime - code compiled. no syntax error. no logical error , but sometime when user gives wrong input in that case if don;t have handling then it gives runtime error like 6%0 will give error.

# in case of error execution stops hence need of exception handling
'''
a = 5
b = 0

try:
    print(a / b)
except Exception as w:
    print("unable to divide by zero", w)

print("Hello")

'''

a = 5
b = 0

try:
    print('resource open')
    # k = int(input("Enetr a number"))
    print(a / b)
    # print('resource closed')  # This was not executed as after getting exception hence put this in exception
except Exception as w:
    print("unable to divide by zero", w)
except ZeroDivisionError as w:
    print(w)
except ValueError as w:
    print(w)

finally:  # will be executed any how
    print("resouce closed")
