## https://www.codewars.com/kata/delete-occurrences-of-an-element-if-it-occurs-more-than-n-times/train/python

import unittest
from collections import Counter

def delete_nth(order,max_e):
    reversed = order[::-1]
    counts = Counter(order)
    for key in counts.keys():
        if counts[key] > max_e:
            for j in range(counts[key] - max_e):
                reversed.remove(key)
    return reversed[::-1]


test = unittest.TestCase()

test.assertEquals(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
test.assertEquals(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2])


