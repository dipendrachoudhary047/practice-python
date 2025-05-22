'''
1.
a = 10  # global

def something():
    global b
    b = 20  # local
    a = 15
    print("inside fucntion",a)


something()
print(b) # this will give error
print("outsoide fucntion",a)

'''

even, odd =  count(list)
