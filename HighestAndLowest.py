## https://www.codewars.com/kata/highest-and-lowest/train/python

import unittest

def high_and_low(numbers):
    numbers = list(map(int, numbers.split(" ")))
    return "%i %i" % (max(numbers), min(numbers))

test = unittest.TestCase()

test.assertEquals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
test.assertEquals(high_and_low("1 2 3 4 5"), "5 1")
test.assertEquals(high_and_low("1 2 -3 4 5"), "5 -3")


