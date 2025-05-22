from array import *
# -------------
# vals = array('i', [1, 2, 3, 3])
# print(vals)
# vals.append(8)
# print(vals)
# print(vals.buffer_info())
# print(vals.typecode)
# vals.reverse()
# print(vals)
#
# for i in range(len(vals)):
#     print(vals[i])
#
# for e in vals:
#     print(e)
# -------------

arr = array('i', [])
length = int(input("enter lenth of array"))
for i in range(length):
    x = int(input("Enter the next value"))
    arr.append(x)

print(arr)

search = int(input('Enter a value for which you need to find index ..'))
i = 0
for i in range(len(arr)-1):
    if arr[i] == search:
        index = i
        print(index)
        break





