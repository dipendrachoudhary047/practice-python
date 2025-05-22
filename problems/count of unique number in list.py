class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unqiuenums = []
        for x in nums:
            if x not in unqiuenums:
                unqiuenums.append(x)
                continue

        return len(unqiuenums)



if __name__ == '__main__':
    obj = Solution()
    value = obj.removeDuplicates(nums=[2,3,5,6,6,4,8,8,9,9,10,10])
    print(value)
