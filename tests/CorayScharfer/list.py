# list is mutable - Means we can update it
courses = ['History', 'math', 'physics', 'chem', 'science']
courses2 = ['nam1', 'nam2']

print(courses.index('math'))
print('chem' in courses)

for item in courses:
    print(item, end=', ')

for index, item in enumerate(courses):
    print(index, item)

courses_str = ', '.join(courses)
print(courses_str)
new_list = courses_str.split(', ')
print(new_list)

# print(courses)
# print(len(courses))
# print(courses[0])
# print(courses[0:2]) # first index inclusive and last is excluded
# print(courses[-1])
#
# courses.pop(2)
# print(courses)
# print(courses.count('math'))
# courses.append('test')
# print(courses)
# courses.insert(0,'test1')
# print(courses)
# courses.pop(2)
# print(courses)
#
# courses.extend(courses2) #extend will add course 2 as values noty as a list. So if you do courses[0], it wont give list.
# print(courses)
#
# courses.reverse()
# print(courses)
# courses.sort()
# print(courses)
# courses.sort(reverse=True)
#
#
# num = [4,7,6,5,2,8]
# print(min(num))
# print(sum(num))
