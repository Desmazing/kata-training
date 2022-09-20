# find the indexes of all the uppercase letters


def capitals(word):
    lst = []
    for i in range(len(word)):
        if word[i].isupper():
            lst.append(word.index(word[i], i))
    return lst


def capitals2(word):
    """this is a refactored version of the above"""
    return [i for i,c in enumerate(word) if c.isupper()]


test1 = print(capitals('SoshdPeqVSqntphhcKYsDmUnHtMuJ'))
test2 = print(capitals('aCcCdDD'))
test3 = print(capitals2('abDsE'))
