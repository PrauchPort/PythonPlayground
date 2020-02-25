#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 22:48:40 2020

@author: wojciechprazuch
"""

import array
import random
import time

arr1 = time.time()

arr = array.array('d', (random.random() for i in range(10**7)))

arr2 = time.time()

lis1 = time.time()

lis = [random.random() for i in range(10**7)]

lis2 = time.time()

print('{}'.format(arr2-arr1))

print('{}'.format(lis2-lis1))
