## https://www.codewars.com/kata/persistent-bugger/train/python

import unittest

from functools import reduce

def persistence(n):
    times = 0
    while len(str(n)) > 1:
        digits = [int(d) for d in str(n)]
        n = reduce(lambda x, y: x * y, digits)
        times += 1
    return times



test = unittest.TestCase()

test.assertEquals(persistence(39), 3)
test.assertEquals(persistence(4), 0)
test.assertEquals(persistence(25), 2)
test.assertEquals(persistence(999), 4)
