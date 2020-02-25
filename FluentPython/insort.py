#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 22:40:29 2020

@author: wojciechprazuch
"""

import bisect
import random

random.seed(12)


SIZE = 9

my_list = []

for i in range(SIZE):
    rand = random.randrange(SIZE*3)
    bisect.insort(my_list, rand)
    print("{0:2d} -> {1}".format(rand, my_list))