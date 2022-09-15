import string

def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6: return False
    for i in pin:
        if i in string.punctuation or i in string.ascii_letters: return False
        if i == '\n': return False
    return True


test1 = print(validate_pin('1234'))
test2 = print(validate_pin("-1234"))
test3 = print(validate_pin("1.234"))
test4 = print(validate_pin("00000000"))
test5 = print(validate_pin("a234"))
test6 = print(validate_pin("124234"))
