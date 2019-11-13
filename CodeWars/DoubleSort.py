## https://www.codewars.com/kata/double-sort/train/python

import unittest

def db_sort(arr):
    intList = [x for x in arr if isinstance(x, int)]
    strList = [x for x in arr if isinstance(x, str)]
    return sorted(intList) + sorted(strList)

test = unittest.TestCase()

test.assertEquals(db_sort([6, 2, 3, 4, 5]), [2, 3, 4, 5, 6])
test.assertEquals(db_sort([14, 32, 3, 5, 5]), [3, 5, 5, 14, 32])
test.assertEquals(db_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
test.assertEquals(db_sort(["Banana", "Orange", "Apple", "Mango", 0, 2, 2]), [0,2,2,"Apple","Banana","Mango","Orange"])
test.assertEquals(db_sort(["C", "W", "W", "W", 1, 2, 0]), [0,1,2,"C","W","W","W"])
test.assertEquals(db_sort(['come', 'on', 110, '2500', 10, '!', 7, 15, 5, 6, 6]), [5,6,6,7,10,15,110,"!","2500","come","on"])
