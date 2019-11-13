##

import unittest

def find_it(seq):
    return [x for x in set(seq) if seq.count(x) % 2 == 1][0]


test = unittest.TestCase()

test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
