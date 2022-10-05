#  check whether an input is a digit between 0-9


import re


def check_digit(n):
    """function uses string.isdigit() method to check if n is a digit
    extra condition is the length of 1"""

    return n.isdigit() and len(n) == 1


def check_digit2(n):
    """function uses regex match method to find a decimal match"""

    return bool(re.match('\d\Z', n))


def check_digit3(n):
    """function uses regex fullmatch method"""

    return bool(re.fullmatch(r'\d', n))


check_digit4 = lambda n: len(n) == 1 and n in '0123456789'
""" uses lambda expressions """


test1 = print(check_digit('1'))
test2 = print(check_digit2('1'))
test3 = print(check_digit('n'))
test4 = print(check_digit2('n'))
test5 = print(check_digit('14'))
test6 = print(check_digit2('14'))
test6 = print(check_digit4('14'))
