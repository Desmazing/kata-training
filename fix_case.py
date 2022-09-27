#  make minimal changes to a string to convert it to all uppercase or lowercase


def fix_case(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isupper(): upper += 1
        elif i.islower(): lower += 1
    if lower >= upper:
        return s.lower()
    return s.upper()


test1 = print(fix_case('CODe'))
test2 = print(fix_case('code'))
test3 = print(fix_case('coDE'))
test4 = print(fix_case('Code'))
