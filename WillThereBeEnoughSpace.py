## https://www.codewars.com/kata/product-of-consecutive-fib-numbers/train/python

import unittest

def enough(cap, on, wait):
    return max(0, wait - (cap - on))

test = unittest.TestCase()

test.assertEquals(enough(10, 5, 5), 0)
test.assertEquals(enough(100, 60, 50), 10)
test.assertEquals(enough(20, 5, 5), 0)

