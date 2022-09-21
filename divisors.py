def divisors(n):
    return len([i for i in range(1,n+1) if n%i==0])


divisors2 = lambda n: sum([n%i == 0 for i in range(1,n+1)])


test1 = print(divisors(1))
test2 = print(divisors(5))
test3 = print(divisors2(10))
