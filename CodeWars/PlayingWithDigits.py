# https://www.codewars.com/kata/playing-with-digits/train/python

import unittest
import math


def dig_pow(n, p):
    factors = [int(math.pow(x, i+p)) for i, x in enumerate(list(map(int, str(n))))]
    return sum(factors) / n if sum(factors) % n == 0 else -1


test = unittest.TestCase()

test.assertEquals(dig_pow(89, 1), 1)
test.assertEquals(dig_pow(92, 1), -1)
test.assertEquals(dig_pow(46288, 3), 51)
