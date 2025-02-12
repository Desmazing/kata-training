"""Return True for None"""


def none(lst, func):
    """Function for enumerable magic"""
    func(i for i in lst)


none([], lambda x: x > 100) # should return True
none([6,5,2,5,2,7], lambda x: x > 9) #, False)
none([6,5,2,5,2,7], lambda x: x % 2 > 0) # False)
none([6,5,2,5,2,7], lambda x: x % 2 == 0) # False)
