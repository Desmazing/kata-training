"""This is an encryption module whereby all the odd indexed characters
are concatenated with all the even indexed characters in a string
Example:
    Input string: Hello
    Number of times to encrypt: 2
        Encyption 1: elHlo
        Encryption 2: lleHo
        Output: 'lleHo'
"""


from itertools import zip_longest


def encrypt(text, n):
    """Function to concatenate all the odd indexed characters in a string
    with all the even indexed characters in the string
    Args: str > input string to be encrypted, int > No. of times to encrypt
    Returns: str > The output string after encryption
    """
    if n == 0:
        return text

    evens = [j for i,j in enumerate(text) if not i % 2]
    odds = [j for i,j in enumerate(text) if i % 2]
    new_text = ''.join(odds + evens)
    return encrypt(new_text, n-1)


def decrypt(text):
    """Function to reverse the above encryption algorithm step by step"""
    text_list = list(text)
    odd_indexed = text_list[:len(text_list) // 2]
    even_indexed = text_list[len(text_list) // 2:]

    new_str = ''.join(str(a) + str(b) for a, b in zip_longest(even_indexed, odd_indexed, fillvalue=''))
    return new_str


print(repr(decrypt("elHlo")))
print(repr(decrypt("ieLn")))

print(repr(encrypt("Hello", 0)))
print(repr(encrypt("Hello", 1)))
print(repr(encrypt("Hello", 2)))
print(repr(encrypt("Hello", 3)))
