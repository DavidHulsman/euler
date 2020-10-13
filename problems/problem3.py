import math


# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# My original pseudocode for this excersize
# get largest prime factor
#   get prime factors
#   divide by first prime, if possible (meaning, it can in fact wholy divide n) save that prime in a list
#   else find next prime and divide by that.
#   return the biggest found prime
def is_prime(n: int) -> bool:
    """
    Input an integer and return True if it is prime.
    Adapted from https://en.wikipedia.org/wiki/Primality_test#Pseudocode
    """
    if n == 2 or n == 3:
        return True
    elif n <= 1 or not n % 2 or not n % 3:
        return False

    i = 5
    while i * i <= n:
        if not n % i or not n % (i + 2):
            return False
        i += 6
    return True


def find_factors(n: int) -> list:
    """
    :param n: Integer
    :return: List of all primes up until sqrt(n)
    """
    if n < 0:
        return []

    primes = []
    for i in range(0, math.floor(math.sqrt(n))):
        if is_prime(i):
            primes.append(i)
    return primes


def largest_prime_factor(n: int) -> int:
    """
    Not that this is a very fragile function and can only end if n is wholy divisible by p

    :param n: The number you want to find the largest prime factor for
    :return: The largest prime factor found
    """
    primes = find_factors(n)
    answers = []
    while n > 2:
        for p in primes:
            if not n % p:
                n //= p
                answers.append(p)
                break
    return max(answers)


# print(find_factors(10 ** 100))
print(find_factors(23185726946653881462851080629414063086870185581))

