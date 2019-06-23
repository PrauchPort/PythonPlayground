## https://www.codewars.com/kata/are-they-the-same/train/python

import unittest

def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    squared = [x*x for x in array1]
    a, b = sorted(squared), sorted(array2)
    return a == b

test = unittest.TestCase()

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
test.assertEquals(comp(a1, a2), True)
