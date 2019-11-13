# https://www.codewars.com/kata/find-the-unique-number-1/train/python

import unittest


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


test = unittest.TestCase()


test.assertEquals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
test.assertEquals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
test.assertEquals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)