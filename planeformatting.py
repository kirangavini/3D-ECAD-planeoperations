# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 09:32:26 2017

@author: kgavini
"""

z = open('plane.txt')
x = z.read()
y = ' '.join(x.split())
y = y.replace('b ridge', 'bridge')
y = y.replace('br idge', 'bridge')
y = y.replace('bri dge', 'bridge')
y = y.replace('brid ge', 'bridge')
y = y.replace('bridg e', 'bridge')
f = open('plane1.txt','w')
f.write(y)
f.close()