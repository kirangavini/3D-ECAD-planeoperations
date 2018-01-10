# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:20:16 2017

@author: kgavini
"""

l1 = [-147.124,-74.338]
r1 = [-147.078,-74.356]
l2 = [-147.022, -74.36]
r2 = [-146.726, -74.44]
if not ((l1[0] > r2[0]) or (l2[0] > r1[0]) or (l1[1] > r2[1]) or (l2[1] > r1[1])):
   print('zone ')
else: print('nothing happening')   
