# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:45:24 2017

@author: kgavini
"""

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        
    def getdata(self):
        return self.data
        
    def getnext(self):
        return self.next
        
    def setdata(self,newdata):
        self.data = newdata          
        
    def setnext(self, nextdata):
        self.next = nextdata
        
        
class Unorderedlist:
      def __init__(self):
          self.head = None
          
      def size(self):
          current = self.head
          count = 0
          while current != None:
              count = count +1
              current = current.getnext()
          return count   
      
      def isEmpty(self):
         return self.head == None
          
      
        
        
        
        
        
x = Unorderedlist()
print(x.size())  
print(x.isEmpty())      
        