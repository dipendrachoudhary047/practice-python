dic1 = {'name': 'dipendra', 'code': 123, 'branch': 'cs',
        'courses': ['math', 'science']}

print(dic1['name'])
print(dic1.get('name'))

#add new value
dic1['newkey'] = 'value1'
print(dic1)

#update existing key
dic1['name'] = 'Rahul'
print(dic1)

#update multiple keys
dic1.update({'name':'braj', 'age':31})
print(dic1)

#delete a key
del dic1['age']
print(dic1)

#popping out a key
name = dic1.pop('name') # it deletes and also return value
print(dic1)
print(name)


print(len(dic1))
print(dic1.keys())
print(dic1.values())
print(dic1.items())

# for key, value in dic1.items():
#     print(key, value)
