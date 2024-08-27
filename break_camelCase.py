"""Complete solution so that the function will break up camel casing using a spacing between words"""


def solution1(s):
    new_string = ''

    for letter in s:
        if letter.isupper():
            new_string += ' ' + letter
        else:
            new_string += letter

    return new_string


def solution2(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)


def functionCall():
    fnCall = input("Enter 1 or 2 to run the code: \n")
    if fnCall == 1:
        print(repr(solution1('helloWorld')))
    elif fnCall == 2:
        solution2()


functionCall()
