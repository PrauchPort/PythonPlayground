#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 23:09:59 2020

@author: wojciechprazuch
"""


import array

arr = array.array('h', [-2, -1, 0, 1, 2])

memv = memoryview(arr)
