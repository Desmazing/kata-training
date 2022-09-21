# print out diamonds


def diamond(n):
    if n <=0 or n%2==0: return None
    elif n==1: return '*\n'


test1 = print(diamond(0))
test2 = print(diamond(1))
test3 = print(diamond(2))
test4 = print(diamond(3))
