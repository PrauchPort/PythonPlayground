## https://www.codewars.com/kata/iq-test/train/python

import unittest

def iq_test(numbers):
    numbers = [int(x) for x in numbers.split()]
    isOdd = [x % 2 for x in numbers]
    return isOdd.index(0) + 1 if isOdd.count(0) < isOdd.count(1) else isOdd.index(1) + 1

test = unittest.TestCase()

test.assertEquals(iq_test("2 4 7 8 10"),3)
test.assertEquals(iq_test("1 2 2"), 1)