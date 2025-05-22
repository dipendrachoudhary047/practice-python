number = 65242432


def reverse(number):
    number2 = 0
    while number != 0:
        digit = number % 10
        number2 = number2 * 10 + digit
        number = number // 10
    return number2

value = reverse(number)
print(value)