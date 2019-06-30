# https://www.codewars.com/kata/sort-the-odd/train/python

import unittest


def sort_array(source_array):
    odd = sorted([x for x in source_array if x % 2 == 1], reverse=True)
    return [] if source_array == [] else [x if x % 2 == 0 else odd.pop() for x in source_array]


test = unittest.TestCase()


test.assertEquals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
test.assertEquals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
test.assertEquals(sort_array([]),[])