## https://www.codewars.com/kata/5ad0d8356165e63c140014d4

import unittest

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    if exam > 75 and projects >= 5:
        return 90
    if exam > 50 and projects >= 2:
        return 75
    else:
        return 0



test = unittest.TestCase()

test.assertEquals(final_grade(100, 12), 100, "Wrong")
test.assertEquals(final_grade(85, 5), 90, "Wrong")
test.assertEquals(final_grade(0, 2), 0, "Wrong")