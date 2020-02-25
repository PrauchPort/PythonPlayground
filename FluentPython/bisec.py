#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:54:42 2020

@author: wojciechprazuch
"""

import bisect
import sys

HAYSTACK = [3, 6, 8, 11, 12, 14, 17, 21, 23, 26, 28, 31]
NEEDLES = [0, 4, 5, 9, 13, 16, 21, 27, 32]

ROW_FMT = "{0:2} @ {1:2}      {2}{0:<2d}"


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * "  |"
        print(ROW_FMT.format(needle, position, offset))
        

bisect_fn = bisect.bisect_right

print('DEMO: ', bisect_fn.__name__)
print('haystack -> ', ''.join('%2d ' % n for n in HAYSTACK))
demo(bisect_fn)
    

def grade(score, grades='FDCBA', breakpoints=[60, 70, 80, 90]):
    i = bisect_fn(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

    
