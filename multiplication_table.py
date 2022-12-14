"""
    Return a multiplication table given a limit n
    For instance: if n == 3; return [[1,2,3], [2,4,6],[3,6,9]]
"""


def multable(n):
    """function to create a custom multiplication table
    Args:
        n(int) a limit to the multiplication table
    Returns:
        list of lists
    """

    lst = []
    for i in range(1, n+1):
        x = []
        for j in range(1, n+1):
            x.append(i*j)
        lst.append(x)
    return lst


def multable2(n):
    """function to create a custom multiplication table
        refactored from multable(n)
    Args:
        n(int): a limit for the mult table
    Returns
        list of lists: the multiplication table
    """

    return [[i*j for i in range(1, n+1)] for j in range(1, n+1)]


test1 = print(multable(3))
test2 = print(multable(4))
test3 = print(multable(10))
test4 = print(multable(34))

test5 = print(multable2(3))
test6 = print(multable2(4))
test7 = print(multable2(10))
