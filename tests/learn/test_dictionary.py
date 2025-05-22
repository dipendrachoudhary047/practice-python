#NestedDictionary
prog = {'JS': 'ATOM', 'CS': 'VS', 'Python': ['pycharme', 'sublime'],
        'JAVA': {'JSE': 'Netbeins', 'JEE': 'Eclipse'}}

print(prog['JS'])
print(prog['Python'])
print(prog['Python'][1])
print(prog['JAVA']['JEE'])

def test_dict_methods():
    print(prog.get('JS'))
    print(prog.get('Python'))
    print(prog['JS'])
    print(prog['Python'])
    print(prog.keys())
    prog["JS"]='ATOM1'
    print(prog.get('JS'))
    print(prog.values())
    prog["testingkey"]="testvalue"
    print(prog.keys())
    for key in prog.keys():
        print(f"{key} ':'{prog.get(key)}' ")

    for x,y in prog.items():
        print(x,y)

def test_new_dictionary():
    d = {'navin': 'samsung', 'rahul': 'iphone', 'kiran': 'oneplus'}
    print(d.keys())
    print(d.values())
    print(d['navin'])
    print(d.get('navin'))