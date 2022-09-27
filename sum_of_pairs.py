# given an array of integers and a target sum
# find a pair of integers that add up to the target sum
# interesting use of sets... why do they work more efficiently in this case?


def sum_pairs(ints, s):
    start = set()
    for i in ints:
        if s - i in start:
            return [s-i, i]
        start.add(i)


test1 = print(sum_pairs([1, 4, 8, 7, 3, 15], 8))
test2 = print(sum_pairs([1, -2, 3, 0, -6, 1], -6))
test3 = print(sum_pairs([20, -13, 40], -7))
test3 = print(sum_pairs([1, 2, 3, 4, 1, 0], 2))
