import unittest

def who_is_next(names, r):


test = unittest.TestCase()

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

test.assertEquals(who_is_next(names, 1), "Sheldon")
test.assertEquals(who_is_next(names, 52), "Penny")
test.assertEquals(who_is_next(names, 7230702951), "Leonard")
