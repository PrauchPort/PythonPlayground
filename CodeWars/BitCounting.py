## https://www.codewars.com/kata/bit-counting/train/python

import unittest

def countBits(n):
    binary = "{0:b}".format(n)
    return list(binary).count("1")

test = unittest.TestCase()


test.assertEquals(countBits(0), 0);
test.assertEquals(countBits(4), 1);
test.assertEquals(countBits(7), 3);
test.assertEquals(countBits(9), 2);
test.assertEquals(countBits(10), 2);