# arithematics
# assigmnet
# relational
# logical
# urinary


def test_arithematic():
    x = 10
    y = 5
    print(x + y)
    print(x - y)
    print(x / y)
    print(x * y)
    print(x // y)
    print(x % y)


def test_assignment():
    x = 10
    x += 2  # x=x+2
    print(x)

    x *= 3
    print(x)

    a, b = 5, 6  # assignment in one line
    print(a + b)


def test_urinary_operator():
    n = 7
    print(n)
    n = -n
    print(n)


def test_relational_opertor():
    a = 2
    b = 3
    print(a < b)
    a = b
    print(a >= b)
    print(a, b)
    print(a != b)


# and /or/ not
def test_logical_operator():
    a = 5
    b = 4
    print(a < 8 and b < 5)
    print(a < 8 or b == 0)
    x = True
    print(x)
    y = not x
    print(y)


# complement ~
def test_bitwise_complement_operator():
    print(~12)


def test_bitwise_and():
    print(12 & 13)


def test_bitwise_or():
    print(12 | 13)


def test_xor_operator():
    print(12 ^ 13)

def test_leftshift_operator():
    print(10 << 2)


def test_right_shift_operator():
    print(10 >> 2)

