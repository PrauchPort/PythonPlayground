## https://www.codewars.com/kata/duplicate-encoder/train/python

import unittest

def duplicate_encode(word):
    output = ""
    word = word.lower()
    for char in word:
        if word.count(char) > 1:
            output += ")"
        else:
            output += "("
    return output


def duplicate_encode2(word):
    return ''.join(['(' if word.lower().count(c) == 1 else ')' for c in word.lower()])


test = unittest.TestCase()

test.assertEquals(duplicate_encode("din"), "(((")
test.assertEquals(duplicate_encode("recede"), "()()()")
test.assertEquals(duplicate_encode("Success"), ")())())", "should ignore case")
test.assertEquals(duplicate_encode("(( @"), "))((")
test.assertEquals(duplicate_encode("nz Ik@Qk!xQRRb(GQIR"), "((())())(()))((()))")


test.assertEquals(duplicate_encode2("din"), "(((")
test.assertEquals(duplicate_encode2("recede"), "()()()")
test.assertEquals(duplicate_encode2("Success"), ")())())", "should ignore case")
test.assertEquals(duplicate_encode2("(( @"), "))((")
test.assertEquals(duplicate_encode2("nz Ik@Qk!xQRRb(GQIR"), "((())())(()))((()))")


