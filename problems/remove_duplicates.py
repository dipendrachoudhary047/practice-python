'''

Remove all duplicates from a list
lst = [1, 2, 2, 3, 4, 4, 5]
 Output: [1, 2, 3, 4, 5]

'''

list = [4,5,6,8,9,7,6,5,5,2,3]
list2 = []

for x in list:
    if x not in list2:
        list2.append(x)

print(list2)

