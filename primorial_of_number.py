"""This module is used to determine the primorial of a number
The primorial of a number is somewhat similar to its factorial
However, only the first n prime numbers are multiplied in this case
Example to demonstrate the distinction:
    Factorial of 7 = 7!  = 1*2*3*4*5*6*7 = 5040
    Primorial of 7 = P#7 = 2*3*5*7*11*13*17 = 510510

Bugs:   Not memory-efficient
        Limited to prime numbers upto 997
"""


import math


def num_primorial(num):
    """Function to determine the primorial of a number
    args: int > the number of primes to be multiplied
    returns: int > the product of the prime number
    """
    return math.prod(list_n_primes()[:num])


def list_n_primes():
    """Function to list all prime numbers from first to the given number
    args: int > the given number of primes to list
    returns: list > a list of prime numbers
    """
    prime_list = []
    for number in range(2, 1000):
        for divisor in range(2, number + 1):
            if number % divisor and number != divisor:
                continue
            if not number % divisor and number != divisor:
                break
            prime_list.append(number)

    return prime_list


print(repr(len(list_n_primes())))
print(repr(num_primorial(20))) # should equal 557940830126698960967415390
print(repr(num_primorial(3))) # should equal 30
print(repr(num_primorial(1))) # should equal 2
print(repr(num_primorial(168)))
