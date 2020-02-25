#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 23:20:01 2020

@author: wojciechprazuch
"""

import random
import time
import numpy as np

arr = np.random.randint(0, 10, size=[2000000, 5])


def count_how_many(x, minimum = 2, maximum = 4):
    count = 0
    for item in x:
        if minimum <= item <= maximum:
            count += 1
    return count


print('Done')

t1 = time.time()

res = [count_how_many(row) for row in arr]

t2 = time.time()

print('Time elapsed: {}'.format(t2-t1))



import multiprocessing as mp

pool = mp.Pool(mp.cpu_count())

t1 = time.time()

res = [pool.map(count_how_many, [row for row in arr])]


t2 = time.time()

print('Time elapsed: {}'.format(t2-t1))