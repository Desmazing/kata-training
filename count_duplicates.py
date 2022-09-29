# count number of distinct letters with count greater than 1


def duplicate_count(text):
    """complete solution
    to be refactored"""
    text = text.lower()
    distinct = set()
    for i in text:
        if text.count(i) > 1:
            distinct.add(i)
            continue
    return len(distinct)


def duplicate_count2(text):
    """this is a refactored version"""
    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])


test1 = print(duplicate_count('abcde'))
test2 = print(duplicate_count('indivisible'))
test2 = print(duplicate_count2('aabbccddefgh'))
