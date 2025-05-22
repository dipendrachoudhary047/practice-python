"""
1. Given a list of integers and a target sum, write a function to find the indices of the two numbers
in the list that add up to the target sum. You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

Example:
int[] nums = {3, 2, 4}
target=6;
Output: [1, 2]
"""

nums = [3, 2, 4, 6, 9, 7, 5, 4, 6]
target = 15

for i in range(len(nums) - 1):
    for j in range(i + 1, (len(nums))):
        if nums[i] + nums[j] == target:
            print("indices are", i, j)
            break
        j = j + 1
    i = i + 1
