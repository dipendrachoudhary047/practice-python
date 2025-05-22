# Write code to filter duplicate elements from an array and print as a list.

list1 = [2, 5, 6, 7, 8, 9, 3, 4, 5, 19, 6, 7, 8, 6, 7, 8, 4, 5, 5, 5, 5, 19]

count_dict = {}
list2 = []

for item in list1:
    if item in count_dict.keys():
        count_dict[item] += 1
    else:
        count_dict[item] = 1

for key, value in count_dict.items():
    if value > 1:
        list2.append(key)

print(count_dict)
print(list2)
