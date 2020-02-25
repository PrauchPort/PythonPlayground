#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 22:57:49 2020

@author: wojciechprazuch
"""


from numba import jit
import numpy as np

x = np.arange(1000).reshape(10, 100)


@jit(nopython=True)
def go_fast(x):
    trace = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            trace += np.tanh(x[i,j])
    return x + trace


def go_fast2(x):
    trace = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            trace += np.tanh(x[i,j])
    return x + trace

start = time.time()
go_fast(x)
end = time.time()
print("Elapsed (with compilation) = %s" % (end - start))

# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed (after compilation) = %s" % (end - start))

start = time.time()
go_fast2(x)
end = time.time()
print("Normal = %s" % (end - start))