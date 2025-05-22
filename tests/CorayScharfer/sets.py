# No duplicate
# No indexing - will get random result each time you print
# Random Values

set1 = {'hindi', 'maths', 'english', 'maths', 'science'}
set2 = {'test1', 'maths', 'test2'}
print(set1)
print('maths' in set1)

print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))
