# Write a python program for String Anagram (multiple approaches).
# "listen" and "silent" → ✅ Anagrams
# "triangle" and "integral" → ✅ Anagrams
# "hello" and "world" → ❌ Not anagrams

# solution1
def is_anagram(string1, string2):
    if sorted(string1) == sorted(string2):
        print("strings are anagram")
    else:
        print("String no anagram")


# solution2
def is_anagram_1(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    if len(string1) != len(string2):
        print("Strings not anagram, different lenght")
        return

    for char in string1:
        if string1.count(char) != string2.count(char):
            print("string not anagram")
            return
    print("string are anagram")


is_anagram(string1='listen', string2='silent')
is_anagram_1('listen', 'silent')
