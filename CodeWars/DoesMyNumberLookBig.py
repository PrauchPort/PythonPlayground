## https://www.codewars.com/kata/does-my-number-look-big-in-this/train/python

import unittest
import math

def narcissistic(value):
    length = len(str(value))
    return value == sum([math.pow(int(x), length) for x in str(value)])


test = unittest.TestCase()

test.assertEquals(narcissistic(7), True, '7 is narcissistic');
test.assertEquals(narcissistic(371), True, '371 is narcissistic');
test.assertEquals(narcissistic(122), False, '122 is not narcissistic')
test.assertEquals(narcissistic(4887), False, '4887 is not narcissistic')