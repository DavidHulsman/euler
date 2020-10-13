from unittest import TestCase

from problems.problem4 import *


class TestLargestPalindrome(TestCase):
    def test_largest_palindrome(self):
        """
        Originally, the starting point was 0,0, but that took more than a second,
        so the starting point has now shifted closed to the end goal
        """
        self.assertEquals(largest_palindrome(90, 90, 91, 99), 9009)
        self.assertEquals(largest_palindrome(900, 989, 999, 999), 906609)
