# find the indexes of all the uppercase letters


def capitals(word):
    lst = []
    for i in range(len(word)):
        if word[i].isupper():
            lst.append(word.index(word[i], i))
    return lst



test1 = print(capitals('SoshdPeqVSqntphhcKYsDmUnHtMuJ'))
test2 = print(capitals('aCcCdDD'))
