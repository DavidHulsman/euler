# Largest palindrome product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

# test number for palindromicity
# go to next number


def largest_palindrome(x: int, y: int, end_x: int, end_y: int) -> int:
    answer = 0
    while y <= end_y:
        while x <= end_x:
            if str(x * y) == str(x * y)[::-1] and x * y > answer:
                answer = x * y
            x += 1
        x = 0
        y += 1
    return answer
