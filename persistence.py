# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative 
# persistence, which is the number of times you must multiply the digits in num until you reach a single digit.


def persistence(num):
    a = list(map(int, list(str(num))))
    lst = []
    prod = 1
    count = 0
    for i in range(len(a)):
        prod *= a[i]
        if a[i] == a[-1]: lst.append(prod)

    count += 1
    return count

