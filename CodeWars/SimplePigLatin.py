## https://www.codewars.com/kata/simple-pig-latin/train/python

import unittest

def pig_it(text):
    lists = [list(x) for x in text.split()]
    moved = [''.join(element[1:] + list(element[0]+ 'ay')) if element[0].isalpha() else element[0] for element in lists]
    return ' '.join(moved)


test = unittest.TestCase()

test.assertEquals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
test.assertEquals(pig_it('This is my string'),'hisTay siay ymay tringsay')