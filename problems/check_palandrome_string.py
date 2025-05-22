#Check if a string is a palindrome
#Input: "madam" → Output: True
#Level == level

def check_palandrome(string1):
    rev_string = ''
    for char in string1:
        rev_string = char+rev_string

    if string1 == rev_string:
        print("String is palandromr")
    else:
        print("String is not palandrome")


check_palandrome('level')


