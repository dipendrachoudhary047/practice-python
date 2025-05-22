# def sum(a, *b):
#     # b will be tuple here hence c = a + b this will not work
#     c = a
#     for i in b:
#         c = c + i
#     print(c)
#
#
# sum(1, 6, 7, 8)

def person(name, *data):
    print(name)
    print(data)


person('navin', 31, 'Biaora', 9981757522)


def persona(name, **kwargs):
    print(name)
    for i, j in kwargs.items():
        print(i, j)


persona('navin', age=31, city='Biaora', phone=9981757522)
