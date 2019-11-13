## https://www.codewars.com/kata/human-readable-time/train/python

import unittest
import math

def make_readable(seconds):
    hours = math.floor(seconds/3600)
    minutes = math.floor((seconds - math.floor(hours*3600)) / 60)
    secs = seconds - hours*3600 - minutes*60
    return "%s:%s:%s" % (str(hours).zfill(2), str(minutes).zfill(2), str(secs).zfill(2))

test = unittest.TestCase()

test.assertEquals(make_readable(0), "00:00:00")
test.assertEquals(make_readable(5), "00:00:05")
test.assertEquals(make_readable(60), "00:01:00")
test.assertEquals(make_readable(86399), "23:59:59")
test.assertEquals(make_readable(359999), "99:59:59")