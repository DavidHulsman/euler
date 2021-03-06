# Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#     1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def sum_of_even_values(n: int) -> int:
    a = 1
    b = 1
    summation = 0

    while a < n and b < n:
        a += b
        if not a % 2:
            summation += a
        b += a
        if not b % 2:
            summation += b
    return summation
