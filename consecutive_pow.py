# take a range of numbers... sum the digits in each raised to the consecutive powers
# return a list


def consecutive_pow(a,b):
    lst = []
    for i in range(a, b+1):
        a = list(str(i))
        mult = 0
        for j,k in enumerate(a):
            mult += int(k) ** (j+1)
            if mult == i: lst.append(i)
    return lst



def consecutive_pow2(a,b):
    """this is a refactored version"""
    return [x for x in range(a, b+1) if sum(int(d)**i for i,d in enumerate(str(x), 1)) == x]


test1 = print(consecutive_pow(1,10))
test2 = print(consecutive_pow(1,100))
test3 = print(consecutive_pow2(10,89))
