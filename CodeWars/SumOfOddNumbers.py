## https://www.codewars.com/kata/sum-of-odd-numbers/train/python

import unittest

def row_sum_odd_numbers(n):
    if n == 1: return 1
    whichOddNumberToStart = sum([x for x in range(n)])+1
    start = 2*whichOddNumberToStart - 1
    summed = 0
    for i in range(n):
        summed += start + 2*i
    return summed


test = unittest.TestCase()

test.assertEquals(row_sum_odd_numbers(1), 1)
test.assertEquals(row_sum_odd_numbers(2), 8)
test.assertEquals(row_sum_odd_numbers(13), 2197)
test.assertEquals(row_sum_odd_numbers(19), 6859)
test.assertEquals(row_sum_odd_numbers(41), 68921)