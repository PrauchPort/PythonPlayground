## https://www.codewars.com/kata/descending-order/python

import unittest
import math

def power_of_two(x):
    return x != 0 and x & (x-1) == 0

test = unittest.TestCase()

test.assertEquals(power_of_two(0), False)
test.assertEquals(power_of_two(1), True)
test.assertEquals(power_of_two(2), True)
test.assertEquals(power_of_two(5), False)
test.assertEquals(power_of_two(6), False)
test.assertEquals(power_of_two(4096), True)

