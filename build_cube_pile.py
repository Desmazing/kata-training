# these two functions simulate the implementation of a stack of cubes 
# such that the top most cube is 1 in volume
# only perfect stacks are considered.


def find_nb(m):
    total = 0
    counter = 0
    nb = 1
    while total != m:
        total += nb ** 3
        counter += 1
        nb += 1
        if total > m: break
    return counter if total == m else -1


def find_nb2(m):
    total = 0
    counter = 0
    for i in range(1, m):
        total += i ** 3
        counter += 1
        if total == m: return counter
    return -1


test = print(find_nb(4183059834009)) # should return 2022
test2 = print(find_nb2(4183059834009)) # should return 2022
test2 = print(find_nb(24723578342962)) # should return -1
