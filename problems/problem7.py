# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

# No peudocode this time. I copied shit from problem 3 and adapted it to this one.

from problems.problem3 import is_prime


def findallprimes(n: int):
    """
    :param n: Integer
    :return: List of primes up until sqrt(n)
    """
    primes = []
    for i in range(0, n):
        if is_prime(i):
            primes.append(i)
        # stop if you've found more than 10001 primes
        if len(primes) > 10002:
            break
    return primes


# print the 10001th prime
# 10000**2 is just meant as a 'very large number'
print(findallprimes(10000 ** 2)[10000])
