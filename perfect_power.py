""" what is a perfect power? 
    n is deemed a perfect power if it is a positive integer 
    and there exists m > 1 and k > 1; such that m ^ k == n
"""


import math
from sympy import perfect_power


def is_perfect_power(n):
    """function computes whether a given integer is a perfect power
        highly inefficient for large values of n.
    Args: 
        n(int): an integer number
    Returns: 
        list [m, k]: a pair of integers that result in the perfect power n
                i.e  m ^ k == n
        or None
    """

    for i in range(1,n+1):
        for j in range(2, int(n**0.5) + 10):
            if i ** j == n:
                return [i, j]
    return None


def is_perfect_power2(n):
    """this is more efficient compared to is_perfect_power()
        still not functional for all cases."""

    for i in range(2, 35):
        if int(n ** (1/i)) == n ** (1/i):
            return [n ** (1/i), i]
    return None


def is_perfect_power3(n):
    """this is the perfect solution
        utilises the perfect_power method of the sympy module
        functional for all cases; including large integers
    """
    x,y = perfect_power(n)
    return [x,y] or None


test1 = print(is_perfect_power(4))
test2 = print(is_perfect_power(9))
test3 = print(is_perfect_power(81))
test4 = print(is_perfect_power2(32))
test5 = print(is_perfect_power2(8))
test6 = print(is_perfect_power2(10000))
test7 = print(is_perfect_power3(45435424))
test8 = print(is_perfect_power2(531441))
test9 = print(is_perfect_power2(78125))
test10 = print(is_perfect_power2(125))
test11 = print(is_perfect_power3(216))
test12 = print(is_perfect_power3(343))
test13 = print(is_perfect_power3(16850581551))

# test14 = print(is_perfect_power2(16850581551))
