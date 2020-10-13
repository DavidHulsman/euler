from unittest import TestCase

from problems.problem2 import *


class TestSumOfEvenValues(TestCase):
    def test_sum_of_even_values(self):
        self.assertEquals(sum_of_even_values(4000000), 4613732)
