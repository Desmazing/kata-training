# take a number... sum the digits in it raised to the consecutive powers


def consecutive_pow(a,b):
    lst = []
    for i in range(a, b+1):
        a = list(str(i))
        mult = 0
        for j,k in enumerate(a):
            mult += int(k) ** (j+1)
            if mult == i: lst.append(i)
    return lst


test1 = print(consecutive_pow(1,10))
test2 = print(consecutive_pow(1,100))
test3 = print(consecutive_pow(10,89))
