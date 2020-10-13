# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def find_multiples(n: int) -> int:
    summ = 0
    for i in range(n):
        if not i % 3 or not i % 5:
            summ += i
    return summ


print('The sum of all the multiples of 3 or 5 below 1000:', find_multiples(1000))
