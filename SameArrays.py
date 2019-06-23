## https://www.codewars.com/kata/are-they-the-same/train/python

import unittest

def comp(array1, array2):
    try:
        return [i*i for i in sorted(array1)] == sorted(array2)
    except:
        return None

test = unittest.TestCase()

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
test.assertEquals(comp(a1, a2), True)
