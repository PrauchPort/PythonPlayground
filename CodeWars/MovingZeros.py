# https://www.codewars.com/kata/moving-zeros-to-the-end/train/python

import unittest


def move_zeros(array):
    numZeros = [x for x in array if x is not False].count(0)
    return [x for x in array if x != 0 or x is False] + [0] * numZeros


test = unittest.TestCase()


test.assertEquals(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
test.assertEquals(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
test.assertEquals(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
test.assertEquals(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
test.assertEquals(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
test.assertEquals(move_zeros(["a","b"]),["a","b"])
test.assertEquals(move_zeros(["a"]),["a"])
test.assertEquals(move_zeros([0,0]),[0,0])
test.assertEquals(move_zeros([0]),[0])
test.assertEquals(move_zeros([False]),[False])
test.assertEquals(move_zeros([]),[])