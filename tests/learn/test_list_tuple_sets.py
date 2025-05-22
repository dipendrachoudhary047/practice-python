# List [] - mutable , ordered, we can change values through indexing
# Tuple () - immutable ,ordered,  iteration faster than list
# set {} - No duplicate, unordered, No Sort , No Sequence, No indexing, immutable


def test_learn_lists():
    names = ['dipendra', 'arjun', 'raghav', 'kiran', 'testing']
    print(names)
    print(names[3])
    names.sort()
    print(names)
    names.reverse()
    print(names)

    mix = [1, 2, 'kirna', 10.6, 'student', 98, 10.5]
    print(mix)

    # merging two lists
    merg = [names, mix]
    print(merg)

    nums = [2, 5, 3, 7, 34, 7, 5, 43, 2, 34]
    print(nums)
    nums[2]=6 # mutable will not give error in assignment
    print(nums)
    listvalues= [2,5,7,8,9,3,45,6,6,78,98,71]
    print(listvalues)




def test_learn_tuples():
    names = ('dipendra', 'arjun', 'raghav', 'kiran', 'testing')
    print(names)
    nums = (2,5,3,7,34,7,5,43,2,34)
    print(nums)
    # nums[2]=6 #tuple immutable will give error
    for x in names:
        print(x)



def test_learn_sets():
    setvalue = {1,2,4,5,6,7,7,7,7,7,32,87,43}
    print(setvalue) #no duplicate , no sequencing

