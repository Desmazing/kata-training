""" Compare the sum of string characters to determine 
    whether they are equal or not. 
    Conditions: All are uppercase, any non-string char voids entire string
    Return True is equal...false otherwise
"""


import string


def compare(str1, str2):
    """Function to determine whether the char code sum of 3 strings are equal
    Args: str > two strings to be compared
    Returns: bool > True if sums equal...false if sums different
    """
    sum1, sum2 = 0, 0
    # str1, str2 = str1.upper(), str2.upper()
    # if any(str1) not in string.ascii_uppercase:
    #     sum1 = 0
    # if any(str2) not in string.ascii_uppercase:
    #     sum2 = 0
    for ch in str1.upper():
        if ch not in string.ascii_uppercase:
            sum1 = 0
            break
        sum1 += ord(ch)
    for ch2 in str2.upper():
        if ch2 not in string.ascii_uppercase:
            sum2 = 0
            break
        sum2 += ord(ch2)
    return sum1 == sum2


print(repr(compare("hello", "hello")))
print(repr(compare("hello", "world")))
print(repr(compare("/snjfd", "sdfm,saadf")))
print(repr(compare("2", "5")))
print(repr(compare("/", ".")))
print(repr(compare("hello", "g4")))
