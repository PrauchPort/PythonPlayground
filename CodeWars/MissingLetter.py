# https://www.codewars.com/kata/find-the-missing-letter/train/python

import unittest


def find_missing_letter(chars):
    to_asci = [ord(char) for char in chars]
    missing = set(range(min(to_asci), max(to_asci)+1)).difference(set(to_asci)).pop()
    return chr(missing)


test = unittest.TestCase()


test.assertEquals(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')
test.assertEquals(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')
