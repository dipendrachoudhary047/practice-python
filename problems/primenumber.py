#checking number is promie using else with for

x =61
for i in range(2, int((x/2)+1)):
    if x % i == 0:
        print("number is not prime")
        break
else:
    print("number is prime")

