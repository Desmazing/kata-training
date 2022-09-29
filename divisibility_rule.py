def thirt(n):
    lst = [1,10,9,12,3,4] * 4
    p = str(n)[::-1]
    output = 0
    while output != int(p[::-1]):
        for i in range(len(p)):
            output += int(p[i]) * lst[i]
        p = str(output)[::-1]
    return output


test1 = print(thirt(8529))
test2 = print(thirt(5634))
