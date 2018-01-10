# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:08:01 2017

@author: kgavini
"""

def InsideTriangle(P,p1,p2,p3): #is P inside triangle made by p1,p2,p3?
    x,x1,x2,x3 = P[0],p1[0],p2[0],p3[0]
    y,y1,y2,y3 = P[1],p1[1],p2[1],p3[1]
    full = area(x1,x2,x3,y1,y2,y3)
    first = area(x,x1,x2,y,y1,y2)
    second = area(x,x2,x3,y,y2,y3)
    third = area(x,x3,x1,y,y3,y1)
    total = first+second+third
    return (total == full)  

def area(x1,x2,x3,y1,y2,y3):
    return abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))

area(56.19,52.14,55.08,46.35,42,44.97)

#print(InsideTriangle((0,5),(-10,0),(10,0), (0,10)))




  
    
    



  