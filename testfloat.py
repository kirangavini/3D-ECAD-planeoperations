# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:17:34 2017

@author: kgavini
"""
capval = '12'
capval1 ='1'
try:
  cval = float(capval)
except ValueError:
  capval = capval
           
try:
  cval = float(capval1)
except ValueError:
  capval1 = capval1 
  