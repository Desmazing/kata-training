import string


def rot13(message):
    output = ''
    up = string.ascii_uppercase * 2
    low = string.ascii_lowercase * 2
    for i in message:
        if str(i) in up:
            output += up[up.index(i) + 13]
        elif str(i) in low:
            output += low[low.index(i) + 13]
        else: output += str(i)
    return output


test1 = print(rot13('test'))
