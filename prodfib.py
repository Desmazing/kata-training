#  Product of consecutive Fibonacci numbers
#  search to ascertain that a number is the product of two consecutive Fibonacci numbers

def prodFib(num):
    counter = 0
    n = [0,1]
    if num == 0: return [0, 1, True]
    for i in range(num):
        n.append(n[-1] + n[-2])
        if n[-1] * n[-2] == num:
            return [n[-2], n[-1], True]
        elif n[-1] * n[-2] > num: return [n[-2], n[-1], False]

test1 = print(prodFib(4895))
test2 = print(prodFib(0))
