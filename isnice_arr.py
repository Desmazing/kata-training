"""This module is used to determine whether an array is nice
what is a nice array:
    A nice array is one where for an element in the array 
    there exists another element where abs(element1 - element2) = 1
    This is true for all array elements
"""


def isnice(arr):
    """Function to determine whether an array is nice or not
    Args    : List > an array of integer elements
    Returns : Bool > True for a nice array and False otherwise
    """
    arr = sorted(arr)
    for j in arr:
        x, y = j+1, j-1
        if x not in arr and y not in arr:
            return False

    return True and len(arr) > 0


print(repr(isnice([2,10,9,3]))) # should return True
print(repr(isnice([3,4,5,7]))) # should return False
print(repr(isnice([]))) # should return False
