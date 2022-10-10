"""
    Abbreviate appropriately. e.g. internationalization == i18n
"""


from string import *
import re


regex = re.compile('[a-z]{4,}', re.IGNORECASE)


def replace(match):
    word = match.group(0)
    return word[0] + str(len(word) - 2) + word[-1]


def abbreviate(s):
    """function to abbreviate words
    Args:
        s (str)
    Returns:
        str: shortened word / sentence
    """
    return regex.sub(replace, s)



test1 = print(abbreviate('internationalization'))
test2 = print(abbreviate('accessibility'))
test3 = print(abbreviate('Accessibility'))
test4 = print(abbreviate('the :'))
test5 = print(abbreviate('elephant-ride'))
