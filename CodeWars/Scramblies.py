## https://www.codewars.com/kata/scramblies/train/python

import unittest
from collections import Counter

def scramble2(s1, s2):
    setS1 = set(list(s1))
    setS2 = set(list(s2))
    countS1 = Counter(s1)
    countS2 = Counter(s2)
    if not setS2.issubset(setS1):
        return False
    for key in countS2:
        if countS2[key] > countS1[key]:
            return False
    return True

def scramble1(s1, s2):
    s1, s2 = list(s1), list(s2)
    for item in s2:
        if item not in s1:
            return False
        s1.remove(item)
    return True

def scramble(s1, s2):
    for item in set(s2):
        if s2.count(item) > s1.count(item):
            return False
    return True


test = unittest.TestCase()

test.assertEquals(scramble('rkqodlw', 'world'),  True)
test.assertEquals(scramble('cedewaraaossoqqyt', 'codewars'), True)
test.assertEquals(scramble('katas', 'steak'), False)
test.assertEquals(scramble('scriptjava', 'javascript'), True)
test.assertEquals(scramble('scriptingjava', 'javascript'), True)