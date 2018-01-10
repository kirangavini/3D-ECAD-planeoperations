# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:06:15 2017

@author: kgavini
"""

import pandas as pd

df = pd.read_csv("point.csv", header = 0) 
df1 = pd.read_csv("verts.csv", header = 0)
xaxis = df.loc[:,'xaxis']
yaxis = df.loc[:,'yaxis']
zaxis = df.loc[:,'zaxis']
index = df.loc[:,'index']

positon1index = df1.loc[:,'position1index']

#for i in positon1index:#range(len(positon1index)):
#   x = []
#   for i in index:
#      xvalue = df.loc[positon1index[i]-1,'xaxis']
#      print(xvalue)
#      x.append(xvalue)
#      #df1['x1'] = pd.Series(df.loc[positon1index[i]-1,'xaxis'], index=[i])   
x = []     
for i in range(len(positon1index)):
    pos_value = positon1index[i]
    #print(pos_value)

    y = df.loc[pos_value-1,'xaxis']
    print(x)
    x.append(y)
    
#x = [df.loc[(positon1index[i])-1,'xaxis'] for i in range(len(positon1index)) ]
