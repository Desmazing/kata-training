# working with lambda functions


def zero(x=None): return 0 if not x else x(0)
def one(x=None): return 1 if not x else x(1)
def two(x=None): return 2 if not x else x(2)
def three(x=None): return 3 if not x else x(3)
def four(x=None): return 4 if not x else x(4)
def five(x=None): return 5 if not x else x(5)
def six(x=None): return 6 if not x else x(6)
def seven(x=None): return 7 if not x else x(7)
def eight(x=None): return 8 if not x else x(8)
def nine(x=None): return 9 if not x else x(9)

def plus(n=None): return lambda a: a + n
def minus(n=None): return lambda a: a - n
def times(n=None): return lambda a: a * n
def divided_by(n=None): return lambda a: a // n


test1 = print(seven(plus(five()))) # should return 12
test2 = print(four(minus(two()))) # should return 2
test3 = print(six(times(seven()))) # should return 42
test4 = print(nine(divided_by(three()))) # should return 3
