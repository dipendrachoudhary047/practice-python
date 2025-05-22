'''
nums = [12, 4, 5, 6, 7, 8, 9]

for i in nums:
    print(i)

# iterator
# converting list to iterator
it = iter(nums)

print(it.__next__())  # will give value
print(it.__next__())  # will give next value

print(next(it)) # will give next value

for i in nums:
    print(i)

'''


class TopTen:
    def __init__(self):
        self.nums = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.nums <= 10:
            val = self.nums
            self.nums += 1
            return val
        else:
            raise StopIteration


values = TopTen()

for i in values:
    print(i)
