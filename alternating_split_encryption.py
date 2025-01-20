"""This is an encryption module whereby all the odd indexed characters
are concatenated with all the even indexed characters in a string
Example:
    Input string: Hello
    Number of times to encrypt: 2

    Encyption 1: elHlo
    Encryption 2: lleHo

    Output: 'lleHo'
"""


def encrypt(text, n):
    """Function to concatenate all the odd indexed characters in a string
        with all the even indexed characters in the string
    Args: str > input string to be encrypted, int > No. of times to encrypt
    Returns: str > The output string after encryption
    """
    x = ''

    for i in range(n, 0, -1):
        x = solver(text)

    return x


def solver(text):
    """Prequel to encrypt"""

    evens = [j for i,j in enumerate(text) if not i % 2]
    odds = [j for i,j in enumerate(text) if i % 2]

    return ''.join(odds + evens)


print(repr(encrypt("what now", 3)))
