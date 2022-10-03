"""
    for a string s:
    if s ends with a digit eg. 'foo1', return a string with the digit incremented by 1 eg. 'foo2'
    if not i.e. 'foo', return s concatenated with '1' i.e. 'foo1' 
"""


def increment_string(s):
    """this solution does not consider edge cases where 
    the digits are in the middle of the string s"""
    if s == '': return ''
    str_part = ''
    digit_part = ''
    for i in s:
        if i.isdigit(): digit_part+= i
        else: str_part += i
    try:
        digit_part = str(int(digit_part) + 1).zfill(len(digit_part))
        return str_part + digit_part
    except ValueError:
        return s + '1'

def increment_string2(s):
    """this solution is applicable for all tests"""
    digit_part = ''    
    for i in s[::-1]:
        if not i.isdigit(): break
        else: digit_part += i
    # print(digit_part)
    try:
        return f'{str(int(digit_part[::-1]) + 1)}'.join(s.rsplit(f'{digit_part}', 1))
    except ValueError:
        return s + '1'


test1 = print(increment_string2('foo')) # should return 'foo1'
test2 = print(increment_string2('')) # should return ''
test3 = print(increment_string('foo24')) # should return 'foo25'
test4 = print(increment_string('hello234')) # should return 'hello235'
test5 = print(increment_string('mane001')) # should return 'mane002'
test6 = print(increment_string('foo99')) # should return 'foo100'
test7 = print(increment_string2('foo99bar99')) # shoudl return 'foo99bar100'
