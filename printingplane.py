# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 13:25:17 2017

@author: kgavini
"""

z = open('plane1.txt')
x = z.read()
y1 = x.split()
j =0
m = open('metals.txt')
m = m.read()
n = ' '.join(m.split())
m = m.split()

for i in range(1,133,2):
    j = j +1
    print('/obj/labels/create screen '+'('+y1[i]+')'+' plane1_die'+str(j))