# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:55:55 2017

@author: kgavini
"""

           

def pairnew(list):
    log = open("plane5join.txt", "w")
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            print('/objects/join-intersect/join screen ('+ list[i] + ' ' + list[j] +') .05 40 yes yes 1', file =log) 
    log.close()        
    return None   



#pairnew(['A','B','C','D'])     


def createnetscreen(filename,y):
    z = open(filename)
    x = z.read().split()
    for i in range(len(x)):
        print('/obj/labels/create screen ('+ x[i] + ') plane'+ str(y) + '_net'+str(i+1))
    return None    

#createnetscreen('metalfaces.txt',5)
    

def createlist(filename):
    z = open(filename)
    x = z.read().split()
    return x
    

listval = createlist('netinfo.txt')    
pairnew(listval)

log = open("netinfo.txt", "w")    
for i in range(1,82): 
  print('plane5_net'+str(i), file =log)
   
log.close()
  


  
        