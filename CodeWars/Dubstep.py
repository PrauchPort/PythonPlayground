## https://www.codewars.com/kata/dubstep/train/python

import unittest

def song_decoder(song):
    return ' '.join(song.replace("WUB", " ").split())


test = unittest.TestCase()

test.assertEquals(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
test.assertEquals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
test.assertEquals(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")