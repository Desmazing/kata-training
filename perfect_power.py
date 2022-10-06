""" what is a perfect power? 
    n is deemed a perfect power if it is a positive integer 
    and there exists m > 1 and k > 1; such that m ^ k == n
"""

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
    pass


test1 = print(is_perfect_power(4))
test2 = print(is_perfect_power(9))
test3 = print(is_perfect_power(81))
test4 = print(is_perfect_power(32))
test5 = print(is_perfect_power(8))
# test6 = print(is_perfect_power(12345234))
