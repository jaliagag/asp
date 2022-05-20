#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 'casd'
b = list(a)

for i in b:
    if i != b[-1]:
        c = b.index(i)+1
        print(b[c])
#    if i == 'c':
#        print(b[i])
        
