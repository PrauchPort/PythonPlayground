#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:18:26 2020

@author: wojciechprazuch
"""

import collections

cnt = collections.Counter('abracadabra')


print(cnt)

cnt.update('aaaaaaabbbbb')

print(cnt)

print(cnt.most_common(4))


class StrKeyDict(collections.UserDict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def __contains__(self, key):
        return self[str(key)]
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item