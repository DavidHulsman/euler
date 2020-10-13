from unittest import TestCase

from problems.problem1 import *


class TestFindMultiples(TestCase):
    def test_find_all_multiples(self):
        self.assertEquals(find_multiples(10), 23)
        self.assertEquals(find_multiples(1000), 233168)
