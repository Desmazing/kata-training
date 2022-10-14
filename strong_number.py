"""
    a strong number is one whose sum of factorial of individual digits is equal to the number
    e.g.
        145 is strong because:
            1! + 4! + 5! = 1 + 24 + 120 ~ 145
        
        7 is not strong because:
            7! = 5040 which is not equal to 7
"""

import math

def strong_number(num):
    """Function to determine a strong number
    Args:       num (int)   positive integer
    Returns:    str : 'Strong!' or not 'Not Strong!'
    """

    total = 0
    for i in str(num):
        total += math.factorial(int(i))
    return "Strong!" if num == total else "Not Strong!"


test1 = print(strong_number(145))   # should return "Strong!"
test2 = print(strong_number(7))     # should return "Not Strong!"
test3 = print(strong_number(9))     # should return "Not Strong!"
