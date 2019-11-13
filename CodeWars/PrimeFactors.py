## https://www.codewars.com/kata/prime-factors-1/train/python

import unittest

def prime_factors(n):
    factors = []
    factor = 2
    while n != 1:
        if n % factor == 0:
            factors.append(factor)
            n /= factor
        else:
            factor += 1
    return factors

test = unittest.TestCase()

test.assertEquals(prime_factors(1),[])
test.assertEquals(prime_factors(2),[2])
test.assertEquals(prime_factors(3),[3])