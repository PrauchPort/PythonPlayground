## https://www.codewars.com/kata/product-of-consecutive-fib-numbers/train/python

import unittest


def productFib(prod):
    n1 = 0
    n2 = 1
    while(n1*n2 < prod):
        prev = n1
        prev2 = n2
        n1 = Fibonnacci(n1, n2)
        n2 = Fibonnacci(n2, n1)
    return [n1, n2, True] if n1 * n2 == prod else [prev2, n1, False]


def Fibonnacci(n1, n2):
    return n1 + n2

test = unittest.TestCase()

test.assertEquals(productFib(4895), [55, 89, True])
test.assertEquals(productFib(5895), [89, 144, False])


