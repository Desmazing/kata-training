def reverse_words(text):
    """this function is not a perfect solution for double spaced words"""
    a = text.split()
    b = []
    for i in a:
        b.append(i[::-1])
    return ' '.join(b)


def reverse_words2(text):
    """this second solution works for double spaced words
    the extra inclusion is the delimitor in the string.split() method"""
    a = text.split(' ')
    b = []
    for i in a:
        b.append(i[::-1])
    return ' '.join(b)


def reverse_words3(text):
    """this is intended to refactor the above two functions"""
    return ' '.join(s[::-1] for s in text.split(' '))


test1 = print(reverse_words('The quick brown fox jumps over the lazy dog.'))
test2 = print(reverse_words3('apple'))
test3 = print(reverse_words3('a b c d')) # should return the same string
test4 = print(reverse_words3('double  spaced  words'))
