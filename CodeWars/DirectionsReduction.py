## https://www.codewars.com/kata/directions-reduction/python

import unittest

def dirReduc(arr):
    deleted = True
    while(deleted):
        deleted = False
        for i in range(len(arr)-1):
            if(set(arr[i:i+2]) == set(["NORTH", "SOUTH"]) or set(arr[i:i+2]) == set(["EAST", "WEST"])):
                del arr[i+1]
                del arr[i]
                deleted = True
                break
    return arr




test = unittest.TestCase()

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
test.assertEquals(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
test.assertEquals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])