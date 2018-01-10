# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:46:18 2017

@author: kgavini
"""

z = open('value.txt')
x = z.read().split()
log = open("zoneinfo.txt", "w") 
for i in range(4297,4453):
        print('/obj/labels/create screen ('+ x[i] + ') plane4'+ '_net'+str(i+1), file = log)
        
        
        
        
A = []
for q in range(1,len(x)+1):
  temp = 'plane4_net' + str(q) 
  A.append(temp)       
  
  

for i in range(0,len(x),2):
    print('/objects/join-intersect/join screen ('+ A[i] + ' ' + A[i+1] +') .05 40 yes yes 1', file = log)
    
log.close()   