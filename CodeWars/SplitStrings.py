## https://www.codewars.com/kata/split-strings/train/python

import unittest

def solution(s):
    return [str(s[i:i + 2]+'_')[:2] for i in range(0, len(s), 2)]


test = unittest.TestCase()

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assertEquals(solution(inp), exp)