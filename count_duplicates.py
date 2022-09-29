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
    return len()


test1 = print(duplicate_count('abcde'))
test2 = print(duplicate_count('indivisible'))
test2 = print(duplicate_count('aabbccddefgh'))
