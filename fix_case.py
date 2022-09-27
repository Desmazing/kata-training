#  make minimal changes to a string to convert it to all uppercase or lowercase


def fixCase(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isupper(): upper += 1
        elif i.islower(): lower += 1
    if lower >= upper:
        return s.lower()
    return s.upper()


def fixCase2(s):
    """this is a refactored version of the above code
    it uses the map function"""
    return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()


test1 = print(fixCase('CODe'))
test2 = print(fixCase('code'))
test3 = print(fixCase2('coDE'))
test4 = print(fixCase2('Code'))
