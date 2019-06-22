## https://www.codewars.com/kata/descending-order/python

import unittest

def Descending_Order(num):
    return int(''.join(sorted(str(num), reverse=True)))

test = unittest.TestCase()

test.assertEquals(Descending_Order(0), 0)
test.assertEquals(Descending_Order(15), 51)
test.assertEquals(Descending_Order(123456789), 987654321)
