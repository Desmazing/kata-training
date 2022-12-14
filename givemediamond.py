"""
    Print out diamonds
"""


def diamond(n):
    if n <=0 or n%2==0: return None
    elif n==1: return '*\n'
    lst = []
    for i in range(1,n+1,2):
        x = (i*'*')
        lst.append(x.center(n).rstrip())
    lst = lst + lst[-2::-1]
    lst.append('\n')
    return '\n'.join(lst)


test0 = print(diamond(0))
test1 = print(diamond(1))
test2 = print(diamond(2))
test3 = print(diamond(3))
test5 = print(diamond(5))
test6 = print(diamond(7))
test7 = print(diamond(9))
