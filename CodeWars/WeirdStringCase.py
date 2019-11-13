## https://www.codewars.com/kata/weird-string-case/train/python

import unittest

def to_weird_word(word):
    return ''.join([letter.upper() if i % 2 == 0 else letter for i, letter in enumerate(word)])

def to_weird_case(string):
    return ' '.join([to_weird_word(word) for word in string.split(' ')])

test = unittest.TestCase()

test.assertEquals(to_weird_case('This'), 'ThIs')
test.assertEquals(to_weird_case('is'), 'Is')
test.assertEquals(to_weird_case('This is a test'), 'ThIs Is A TeSt')
