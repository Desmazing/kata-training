# return a list of anagrams given a word and an array of words
# an anagram is a word or phrase acheived by rearranging the letters of a different word or phrase
# for instance anagrams('abba', ['bbaa', 'aabb', 'abcd', 'efgh', 'abdf'])
# the above case returns ['bbaa', 'aabb']

def anagrams(word, words):
    """this is a more comprehensive solution to the problem."""
    return [term for term in words if sorted(term) == sorted(word)]


def anagrams2(word, words):
    """this is a stepwise solution"""
    ana_list = []
    for term in words:
        if sorted(term) == sorted(word):
            ana_list.append(term)
    return ana_list


test1 = print(anagrams('abba', ['bbaa', 'aabb', 'abcd', 'efgh', 'abdf']))
test2 = print(anagrams2('hello', ['lo', 'lehlo', 'lohel', 'hello', 'hel']))
