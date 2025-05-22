#Solution
#Create a dic with all char and their occurrence count
# then convert into a list
# pick lists 1st element and match with all

class Solution:
    def checkOccurrence(self, s: str) -> bool:
        dict = {}
        for char in s:
            dict[char] = s.count(char)

        value = list(dict.values())
        for x in value:
            if x != value[0]:
                return False
        else:
            return True


# Calling the method in the same file
if __name__ == '__main__':
    obj = Solution()
    value = obj.checkOccurrence("abb")
    print(value)
