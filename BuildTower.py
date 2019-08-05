# https://www.codewars.com/kata/build-tower/train/python

import unittest


def tower_builder(n_floors):
    tower = []
    if n_floors == 1:
        return ['*']
    num_fields = n_floors*2 - 1
    for i in range(n_floors):
        num_stars = 2*i + 1
        num_spaces = num_fields - num_stars
        tower.append(" "*int(num_spaces/2) + "*"*num_stars + " "*int(num_spaces/2))
    return tower


test = unittest.TestCase()


test.assertEquals(tower_builder(1), ['*', ])
test.assertEquals(tower_builder(2), [' * ', '***'])
test.assertEquals(tower_builder(3), ['  *  ', ' *** ', '*****'])