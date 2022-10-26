"""
    return the maximum sum for contiguous elements in an array
"""


def max_sequence(arr):
    """funtion to find the maximum sum for contiguous elements in an array

    Args:       arr (list)  An array of integers
    Returns:    int - maximum sum
    """

    if len(arr) == 0:
        return 0
    sum_list = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sum_list.append(sum(arr[i:j+1]))

    return max(sum_list)


# the above method is not the most efficient. need to refactor.

test0 = print(max_sequence([])) # empty array should return 0
test1 = print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # should return 6
test2 = print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))
# should return 155
test3 = print(max_sequence([8, 6, 12, 9, 3, 13, -14, 15, -16, 14, 15, 18, 17, 2, 20,\
     -13, 10, -5, -4])) # should return 122
test4 = print(max_sequence([18, -13, 17, 15, 12, -13, 16, -1, 4, 7, 8, -10, 15, -7, -6, 16]))
# should return 78
