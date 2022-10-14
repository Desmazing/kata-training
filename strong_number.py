"""
    a strong number is one whose sum of factorial of individual digits is equal to the number
    e.g.
        145 is strong because:
            1! + 4! + 5! = 1 + 24 + 120 ~ 145
        
        7 is not strong because:
            7! = 5040 which is not equal to 7
"""


def strong_number(num):
    """Function to determine a strong number
    Args:       num (int)   positive integer
    Returns:    str : 'Strong!' or not 'Not Strong!'
    """