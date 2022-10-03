"""
    for a string s:
    if s ends with a digit eg. 'foo1', return a string with the digit incremented by 1 eg. 'foo2'
    if not i.e. 'foo', return s concatenated with '1' i.e. 'foo1' 
"""


def increment_string(s):
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


test1 = print(increment_string('foo')) # should return 'foo1'
test2 = print(increment_string('')) # should return ''
test3 = print(increment_string('foo24')) # should return 'foo25'
test4 = print(increment_string('hello234')) # should return 'hello235'
test5 = print(increment_string('mane001')) # should return mane002
test6 = print(increment_string('foo99')) # should return foo100

# ================
# unconsidered edge cases... 'foo99bar99' should return foo99bar100
