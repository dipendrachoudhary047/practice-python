'''
Given a list of integers and a target sum,determine whether there exists a subset of the list that adds up exactly to the
target sum.

    A subset means any combination of elements (not necessarily contiguous).
    You don't have to return the subset, just a True/False answer.
    You can use each element once (not multiple times).

Input: nums = [3, 34, 4, 12, 5, 7], target = 9
Output: True

'''

#this problem is specific to two index
list1 = [3, 34, 4, 12, 5, 2]
target = 14

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] + list1[j] == target:
            print('index are ', i, j)


