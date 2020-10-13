from unittest import TestCase

from problems.problem3 import *


class TestLargestPrimeFactor(TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(-1), "-1 went wrong")

        list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                          97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
                          193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
                          307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
                          421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
                          547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
                          659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
                          797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919,
                          929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

        for n in list_of_primes:
            self.assertTrue(is_prime(n), str(n) + " went wrong")

        # Create list of composites
        list_of_composites = [x for x in range(0, 1001) if x not in list_of_primes]

        for n in list_of_composites:
            self.assertFalse(is_prime(n), str(n) + " went wrong")

    def test_findallprimes(self):
        self.assertEquals(find_factors(-1), [])
        self.assertEquals(find_factors(0), [])
        self.assertEquals(find_factors(1), [])
        self.assertEquals(find_factors(2), [])
        self.assertEquals(find_factors(3), [])
        self.assertEquals(find_factors(4), [])
        self.assertEquals(find_factors(5), [])
        self.assertEquals(find_factors(6), [])
        self.assertEquals(find_factors(7), [])
        self.assertEquals(find_factors(8), [])
        self.assertEquals(find_factors(9), [2])
        self.assertEquals(find_factors(10), [2])
        self.assertEquals(find_factors(50), [2, 3, 5])
        self.assertEquals(find_factors(100), [2, 3, 5, 7])
        self.assertEquals(find_factors(1000), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    # def test_largestprimefactor(self):
    #     self.assertEquals(largest_prime_factor(9), -1)

    def test_answer(self):
        self.assertEquals(13195, 5 * 7 * 13 * 29, "The maths broke!")
        self.assertEquals(largest_prime_factor(13195), 29)
