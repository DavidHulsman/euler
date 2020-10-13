# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# My Pseudocode
# check if n can be evenly divided up to 20
#   print the number and break the loop
# if not, go to next number


def smallest_multiple(upto: int) -> int:
    """ It may be slow, but it's MY code, god damnit! Not to mention that I've been able to cut runtime by HALF!"""
    i = upto
    while True:
        for j in range(3, upto + 1):
            if i % j != 0:
                break
            if j == upto:
                return i
        i += upto


smallest_multiple(20)
