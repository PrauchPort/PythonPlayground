# https://www.codewars.com/kata/which-are-in/train/python

import unittest


def in_array(array1, array2):
    return sorted(set([x for x in array1 for base in array2 if is_substring(list(x), list(base))]))


def is_substring(x, base):
    check = [letter for letter in x if x.count(letter) <= base.count(letter)]
    return True if len(check) == len(x) else False


test = unittest.TestCase()


a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
test.assertEquals(in_array(a1, a2), r)