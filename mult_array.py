# return a multiple of all the elements in an array


def mult(arr):
    mult = 1
    for i in arr:
        mult *= i
    return mult


def mult1(arr):
    """this is a refactored version of the above function"""
