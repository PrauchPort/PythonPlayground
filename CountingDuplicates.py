## https://www.codewars.com/kata/number-shortening-filter/train/python

import unittest


def duplicate_count(text):
    return sum([1 for x in list(set(text.lower())) if x.isalpha() and list(text.lower()).count(x) >= 2])

test = unittest.TestCase()

test.assertEquals(duplicate_count("abcde"), 0)
test.assertEquals(duplicate_count("abcdea"), 1)
test.assertEquals(duplicate_count("indivisibility"), 1)