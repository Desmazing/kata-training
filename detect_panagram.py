# a panagram uses all the letters of the alphabet at least once


import string


def is_panagram(s):
    """check if letters occur to a total of 26. Numbers don't matter"""
    s = s.translate(str.maketrans('','',string.punctuation)).replace(' ','').lower()
    for i in string.ascii_lowercase:
        if i not in s:
            return False
    return True


test1 = print(is_panagram("The quick, brown fox jumps over the lazy dog!"))
test2 = print(is_panagram("1bcdefghijklmnopqrstuvwxyz"))
test3 = print(is_panagram("8abcdefgh234ijklmnopqrs56765tuvwxyz1234"))
