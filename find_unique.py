# find the unique number in an array e.g. [1,2,1,1,1,1] should return 2
# this function is meant for performance efficiency due to large arrays


def unique(n):
    """this version sorts an array. If the first two elements are alike, return the last
    else return the first"""
    a = sorted(n)
    if a[0]==a[1]: return a[-1]
    return a[0]


def unique2(n):
    """this is a refactored version of the above function"""
    a,b = set(n)
    return b


test1 = print(unique([1,2,1,1,1,1])) # should return 2
