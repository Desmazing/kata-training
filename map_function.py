# exploring using the map() function
# the map function returns a map object(iterator) of results after applying function to each item in iterable


def sum_mix(arr):
    """this is a refactored version of the below function sum_mix2()"""
    return sum(map(int, arr))


def sum_mix2(arr):
    """return the sum of the mixed data types in the array
    types are integer and string"""
    total = 0
    for i in arr:
         total+= int(i)
    return total


test1 = print(sum_mix([1,'2']))
test2 = print(sum_mix2([1,2,4,'4','3',6, '7']))
test3 = print(sum_mix([2,'4','5']))
