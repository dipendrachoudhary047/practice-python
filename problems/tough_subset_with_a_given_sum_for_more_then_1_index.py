'''
Given a list of integers and a target sum,determine whether there exists a subset of the list that adds up exactly to the
target sum.

    A subset means any combination of elements (not necessarily contiguous).
    You don't have to return the subset, just a True/False answer.
    You can use each element once (not multiple times).

Input: nums = [3, 34, 4, 12, 5, 2], target = 9
Output: True

Input: nums = [1, 2, 3, 7], target = 6
Output: True  → Subset [1, 2, 3]

Input: nums = [1, 2, 7, 1, 5], target = 10
Output: True  → Subset [2, 1, 7] or [1, 1, 2, 5, ...]

Input: nums = [1, 3, 5, 9], target = 15
Output: False → No subset sums to 15
'''


# this problem is specific to multiple index.

def is_subset_sum(nums, target, index=0):
    print(f"Checking: target={target}, index={index}, remaining={nums[index:]}")

    # Base case 1: success
    if target == 0:
        print("✅ Found a subset!")
        return True

    # Base case 2: failure
    if index == len(nums) or target < 0:
        return False

    # Option 1: Include current number
    include = is_subset_sum(nums, target - nums[index], index + 1)

    # Option 2: Exclude current number
    exclude = is_subset_sum(nums, target, index + 1)

    return include or exclude

nums = [3, 4, 5]
target = 9
print("Result:", is_subset_sum(nums, target))