## https://www.codewars.com/kata/5558cc216a7a231ac9000022

import unittest

def duplicates(array):
    duplicates = []
    for i in range(len(array)):
        if array[i] in array[:i] and array[i] not in duplicates:
            duplicates.append(array[i])
    return duplicates

test = unittest.TestCase()

test.assertEquals(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5']), [4, 3, 1], "Wrong")

