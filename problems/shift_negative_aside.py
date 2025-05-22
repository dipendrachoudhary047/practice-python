"""
2. Given an array of integers, write a function to move all the negative numbers
to the left end of the array without changing the relative order of the non-negative numbers.
 The function should do this in place with a minimum number of operations.

Example:
int[] nums = {1, -1, 3, -2, -3, 5, 6, -7}
Output: [-1, -2, -3, -7, 1, 3, 5, 6]
"""

list1 = [1, -1, 3, -2, -3, 5, 6, -7]
list2 = []
for x in list1:
    if x < 0:
        list2.append(x)
for x in list1:
    if x >= 0:
        list2.append(x)

print(list2)
