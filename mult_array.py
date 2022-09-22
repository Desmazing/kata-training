# return a multiple of all the elements in an array


import math


def mult(arr):
    mult = 1
    for i in arr:
        mult *= i
    return mult


def mult1(arr):
    """this is a refactored version of the above function"""
    mult = lambda x, y: x*y, arr
    return mult


def mult2(arr):
    """refactored using math module"""
    return math.prod(arr)


test1 = print(mult([1,2,3]))
test2 = print(mult1([1,2,3]))
test3 = print(mult2([1,2,3]))
