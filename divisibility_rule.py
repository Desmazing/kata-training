lst = [1,10,9,12,3,4]


def thirt(n):
    """complete solution
    need to acquaint with recursion a lot more"""
    strn = str(n)[::-1]
    output = 0
    for i in range(len(strn)):
        output += int(strn[i]) * lst[i % 6]
    if n == output:
        return output
    else: 
        return thirt(output)
    

def thirt2(n):
    """refactor complete"""
    strn = str(n)[::-1]
    m = sum(lst[i % 6] * int(strn[i]) for i in range(len(strn)))
    return n if n == m else thirt(m)


test1 = print(thirt(8529))
test2 = print(thirt(5634))
test3 = print(thirt2(1111111111))
test4 = print(thirt2(987654321))
