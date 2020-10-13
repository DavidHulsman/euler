from unittest import TestCase

from problems.problem5 import *


class TestSmallestMultiple(TestCase):
    def test_smallest_multiple(self):
        self.assertEquals(smallest_multiple(10), 2520)
        # self.assertEquals(smallest_multiple(20), 232792560)
