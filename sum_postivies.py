# this requires us to return the sum of all positive numbers in an array
# and an array of all the negative numbers


def array_sort(arr):
    """this function has too many lines.
    to be refactored"""
    neg = []
    pos = 0
    for i in arr:
        if i < 0: neg.append(i)
        elif i > 0: pos += 1
    return [neg, pos]





test1 = print(array_sort([-1,2,1,3]))
test2 = print(array_sort([]))
