# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
z = open('plane1.txt')
x = z.read()
y = ' '.join(x.split())
y1 = y.split()
size = 66
even = ['']*size
odd = ['']*size
j = 0

for i in range(0,133):
    if i % 2 == 0:
        even[j] = y1[i]
        j = j+1   
    else: odd[j-1] =y1[i] 
                    
   
