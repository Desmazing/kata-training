"""
    A divisibility rule by 7... splitting a number m such that 10x + y = m
    if x - 2y is divisible by 7, then m is divisible by 7
    return (last m, number of executions)
    last m : final calculation whereby m has at most 2 digits

"""


def seven(m, count = 0):
    """function to determine divisibility by 7
    Args:       m (int) 
    Returns:    tuple (last m, number of executions)
    """

    if m < 100: return (m, count)
    y, x = m % 10, m // 10
    count += 1
    result = x - (2 * y)

    return (seven(result, count))


test1 = print(seven(371))
test2 = print(seven(1603))
