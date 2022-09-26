def mults(n):
    return n * n


def comp(array1, array2):
    try:
        res = list(map(mults, sorted(array1)))
        return res == sorted(array2)
    except:
        return False


test1 = print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
test2 = print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361]))
