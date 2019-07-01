# https://www.codewars.com/kata/valid-parentheses/train/python

import unittest


def valid_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0



test = unittest.TestCase()


test.assertEquals(valid_parentheses("  ("),False)
test.assertEquals(valid_parentheses(")test"),False)
test.assertEquals(valid_parentheses(""),True)
test.assertEquals(valid_parentheses("hi())("),False)
test.assertEquals(valid_parentheses("hi(hi)()"),True)