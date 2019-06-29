## https://www.codewars.com/kata/sum-of-digits-slash-digital-root/train/python

import unittest


def digital_root1(n):
    while n > 9:
        digits = [int(x) for x in list(str(n))]
        n = sum(digits)
    return n


def digital_root(n):
    return n if n < 9 else digital_root(sum(map(int, str(n))))


test = unittest.TestCase()

test.assertEquals(digital_root(16), 7)
test.assertEquals(digital_root(456), 6)
