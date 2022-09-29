# count number of distinct letters with count greater than 1


def duplicate_count(text):
    text = text.lower()
    distinct = set()
    for i in text:
        if text.count(i) > 1:
            distinct.add(i)
            continue
    return len(distinct)


test1 = print(duplicate_count('abcde'))
test2 = print(duplicate_count('indivisible'))
test2 = print(duplicate_count('aabbccddefgh'))
