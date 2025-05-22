'''
str = "  dipen draaa  "
# ways to iterate through string
for x in str:
    print(x, end="")

for x in range(len(str)):
    print(str[x], end="")

newstr = ""
for x in range(len(str)):
    newstr = str[x]+newstr
print(newstr)

str1=""
for x in str:
    str1=x+str1
print(str1)

print(str.count('a'))
print(str.split('a'))
print(str.strip())
print(str.lstrip())
print(str.rstrip())

'''

"""
list = [1, 4, 5, 7, 8, 3, 'new', 'number', 67, 8]

for x in list:
    print(x, end="")

for x in range(len(list)):
    print(list[x], end="")

list.append('your')
print(list)
list.reverse()
print(list)
list[1]= 'check'
print(list)
list.insert(0,"test")
print(list)
list.remove('check')
print(list)

"""

dict = {"id": 21, "name": "dipendra", "city": "biaora"}

# for x in dict.items():
#     print(x)
# for x in dict.values():
#     print(x)
# for x in dict.keys():
#     print(x)


dict["id1"] = 54
print(dict)

# for x in dict.keys():
#     print(dict.get(x))
#
# for x,y in dict.items():
#     print(x,y)

for x,y in dict.items():
    if x=='city':
        print(x,y)