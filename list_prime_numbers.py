"""This module is used to list all the prime numbers for a given range"""


def list_primes(n):
    """Function to list all prime numbers from first to the given number
    args: int > the given number of primes to list
    returns: list > a list of prime numbers
    """

    my_list = []

    for number in range(2, n):
        for divisor in range(2, number + 1):
            if number % divisor and number != divisor:
                continue
            elif not number % divisor and number != divisor:
                break
            my_list.append(number)

    return my_list


# def list_primes_version_2(n):
#     """Function to list all prime numbers from first to the given number
#     args: int > the given number of primes to list
#     returns: list > a list of prime numbers
#     """


print(repr(list_primes(100)))
