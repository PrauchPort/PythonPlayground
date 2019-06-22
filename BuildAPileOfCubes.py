## https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

import unittest

def find_nb(m):
    n = 1
    sum = n*n*n
    while sum < m:
        n += 1
        sum += n*n*n
    if sum == m:
        return n
    else:
        return -1

test = unittest.TestCase()

test.assertEquals(find_nb(4183059834009), 2022)
test.assertEquals(find_nb(24723578342962), -1)
test.assertEquals(find_nb(135440716410000), 4824)
test.assertEquals(find_nb(40539911473216), 3568)
test.assertEquals(find_nb(26825883955641), 3218)

