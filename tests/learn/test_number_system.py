#binary 0-1
#decimal (1-9)
#octal 0-7
#hexadecimal - ip address , hash (0-9 and a-f)
from unicodedata import decimal


def test_int_to_binary():
    x=25
    print(bin(x))
    #ob is always starting in binary and poutput will be like 11001

    print(oct(x))
    #start with 0o
    print(hex(x))
    #start with 0x

    y=31
    print(bin(y))

    z=0b110011010
    print(z)







