"""
Implementing a function that takes a string as an argument.
It then shifts every letter by 10 places.
From z, it starts shifting from a again
returns the new string
"""


def move_ten(str):
    """Function that shifts letter of the alphabet by 10 places
    args: 1 > str
    returns: 1 > str
    """
    lst = [ord(i)+10 for i in str]
    lst = [i-26 if i>122 else i for i in lst]
    lst = list(map(chr, lst))

    return ''.join(lst)


def move_ten_v2(str):
    """ Function that shifts each letter in a string by 10 places
        More memory efficient than move_ten()
        args: 1 > str
        returns: 1> str"""

    lst = [chr(ord(i)+10 for i in str)]
    return lst


print(repr(move_ten('testcase'))) #should return 'docdmkco'
print(repr(move_ten('zyxwvut'))) #should return 'jihgfed'

print(repr(move_ten_v2('testcase')))
