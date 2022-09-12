def reverse_words(text):
    """this function is not a perfect solution for double spaced words"""
    a = text.split()
    b = []
    for i in a:
        b.append(i[::-1])
    return ' '.join(b)


test1 = print(reverse_words('The quick brown fox jumps over the lazy dog.'))
test2 = print(reverse_words('apple'))
test3 = print(reverse_words('a b c d')) # should return the same string