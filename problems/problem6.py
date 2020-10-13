# Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 = 385
#
#  The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sosq(n: int):
    answer = 0
    for i in range(1, n + 1):
        answer += i ** 2
    return answer


def sqos(n: int):
    answer = 0
    for i in range(1, n + 1):
        answer += i
    return answer ** 2

sqos1 = sqos(10)
sosq1 = sosq(10)
print(sqos1, '-', sosq1, '=', sqos1 - sosq1)
sqos2 = sqos(100)
sosq2 = sosq(100)
print(sqos2, '-', sosq2, '=', sqos2 - sosq2)