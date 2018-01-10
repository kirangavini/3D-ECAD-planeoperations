# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:21:38 2017

@author: kgavini
"""

import pandas as pd


    # import files and preprocessing
df = pd.read_csv("points.csv") 
df1 = pd.read_csv("verts.csv")
xaxis = df.loc[:,'x']
yaxis = df.loc[:,'y']
zaxis = df.loc[:,'z']
index = df.loc[:,'index']
position1index = df1.loc[:,'position1']
position2index = df1.loc[:,'position2']
position3index = df1.loc[:,'position3']

# filter x and y axis from first data set and append it into second one       
x1 = [df.loc[(position1index[i])-1,'x'] for i in range(len(position1index)) ]
df1['x1'] = pd.Series(x1, index=df1.index)
y1 = [df.loc[(position1index[i])-1,'y'] for i in range(len(position1index)) ]
df1['y1'] = pd.Series(y1, index=df1.index)
x2 = [df.loc[(position2index[i])-1,'x'] for i in range(len(position2index)) ]
df1['x2'] = pd.Series(x2, index=df1.index)
y2 = [df.loc[(position2index[i])-1,'y'] for i in range(len(position2index)) ]
df1['y2'] = pd.Series(y2, index=df1.index)
x3 = [df.loc[(position3index[i])-1,'x'] for i in range(len(position3index)) ]
df1['x3'] = pd.Series(x3, index=df1.index)
y3 = [df.loc[(position3index[i])-1,'y'] for i in range(len(position3index)) ]
df1['y3'] = pd.Series(y3, index=df1.index)  
x3 = [df.loc[(position3index[i])-1,'x'] for i in range(len(position3index)) ]

z1 = [df.loc[(position1index[i])-1,'z'] for i in range(len(position1index)) ]
df1['z1'] = pd.Series(z1, index=df1.index)
z2 = [df.loc[(position2index[i])-1,'z'] for i in range(len(position2index)) ]
df1['z2'] = pd.Series(z2, index=df1.index)
z3 = [df.loc[(position3index[i])-1,'z'] for i in range(len(position3index)) ]
df1['z3'] = pd.Series(z3, index=df1.index)

 

    # remove unwanted columns 
cols = df1.columns.tolist()
cols1 = cols[5:14] +cols[4:5]
df1 = df1[cols1]
            
zoneid = df1.loc[:,'zoneid']


    # append x values to a dictonary and categorize them individually in a seperate list    
xvalues = {}
n = 0
j = []
for i in zoneid:
   if i in j:
       xvalues[i].append([x1[n],x2[n],x3[n]])
   else:
       xvalues[i] = []
       xvalues[i].append([x1[n],x2[n],x3[n]])
       j.append(i)
   n = n+1
    
    
xnumber = [[] for _ in range(len(zoneid))]
for i in xvalues:
   indlist  = xvalues[i]
   for i1 in range(len(indlist)):
     for i2 in range(len(indlist[i1])):
        xnumber[i].append(indlist[i1][i2])


           
           
           
# append y values to a dictonary and categorize them individually in a seperate list   
yvalues = {}
n1 = 0
j1 = []
for i1 in zoneid:
   if i1 in j1:
       yvalues[i1].append([y1[n1],y2[n1],y3[n1]])
   else:
       yvalues[i1] = []
       yvalues[i1].append([y1[n1],y2[n1],y3[n1]])
       j1.append(i1)
   n1 = n1+1    
    
ynumber = [[] for _ in range(len(zoneid))]
for i in yvalues:
   indlist1  = yvalues[i]
   for i1 in range(len(indlist1)):
      for i2 in range(len(indlist1[i1])):
         ynumber[i].append(indlist1[i1][i2])  
         
         
zvalues = {}
n1 = 0
j1 = []
for i1 in zoneid:
   if i1 in j1:
       zvalues[i1].append([z1[n1],z2[n1],z3[n1]])
   else:
       zvalues[i1] = []
       zvalues[i1].append([z1[n1],z2[n1],z3[n1]])
       j1.append(i1)
   n1 = n1+1    
    
znumber = [[] for _ in range(len(zoneid))]
for i in zvalues:
   indlist1  = zvalues[i]
   for i1 in range(len(indlist1)):
      for i2 in range(len(indlist1[i1])):
         znumber[i].append(indlist1[i1][i2])          
           
           
    # find intersection between different zones           
    #value = [1354 1807 1285 1746 625 195 2778 274 1064 85 434 2627 2206 1485 1135 1325 2127 1254 734 1817 1767 714 2417 2567 484 2508 2728 1015 1344 1094 2037 3197 2697 1384 1025 1937 915 1195 2997 1414 705 254 1575 514 264 2638 1055 1624 644 2297 2928 2287 2598 375 674 314 414 2357 655 3078 2578 1827 1274 2257 1445 284 2818 395 2808 535 1144 1535 2547 1404 444 1235 2767 2396 2798 3088 1104 175 3057 2007 305 1906 1264 3007 1525 2137 2747 764 1727 2116 1796 1464 584 2406 2898 1916 545 1956 144 2837 2657 1847 2027 1495 2707 505 2237 3137 135 3028 1717 2968 1205 3128 1455 455 1544 745 334 1987 1504 2197 3148 2977 2857 1084 1375 1976 3108 1594 1124 2878 1185 215 2017 2366 2618 1425 1615 2346 3168 2717 565 2247 944 324 1365 1857 1787 1736 2667 554 244 665 2386 2306 2788 1926 685 234 2757 3157 985 3038 2276 1515 1836 495 1886 595 2518 95 2056 3067 725 2426 475 574 785 2888 1395 164 2828 2146 2737 124 1876 2918 1215 2558 2587 2988 794 1564 1174 954 974 2537 225 2066 3018 1244 385 925 1314 2527 104 2327 1154 1074 994 1997 2377 405 365 1045 2677 2947 1295 1604 754 3118 2167 1335 355 2227 2046 1866 634 2907 344 1005 965 155 2266 615 695 1225 1474 1896 2107 934 2687 3048 1555 524 2608 1034 1756 2958 3187 204 605 2087 294 114 3208 1946 2867 1164 2648 2186 2177 3217 2937 774 1114 1966 424 3177 1584 2337 1776 2156 2097 465 1435 1305 2317 2847 3097 2216 185 2076]
      



def overlap(val1,val2,val3):
    mindif = abs(val1-val2)
    maxdif = abs(val1-val3)
    return ((val1>val2 or mindif <1e-12) and (val1<val3 or maxdif <1e-12))

def rectoverlap(xmin,xmax,ymin,ymax,zmin,zmax,xmin1,xmax1,ymin1,ymax1,zmin1,zmax1):
    xoverlap1 = overlap(xmin,xmin1,xmax1)
    xoverlap2 = overlap(xmin1, xmin, xmax)
    xoverlap = (xoverlap1 or xoverlap2)
    
    yoverlap1 = overlap(ymin,ymin1,ymax1)
    yoverlap2 = overlap(ymin1, ymin, ymax)
    yoverlap = (yoverlap1 or yoverlap2)
    
    zoverlap1 = overlap(zmin,zmin1,zmax1)
    zoverlap2 = overlap(zmin1, zmin, zmax)
    zoverlap = (zoverlap1 or zoverlap2)
    
    return (xoverlap and yoverlap and zoverlap)




       
value1 = open('value.txt')
value1 = value1.read()
value1 = value1.split()
value = [int(i) for i in value1]

    #loop through every possible zone pair and find the intersection  
zoneuniqueval = set(zoneid)
zoneuniqueval = list(zoneuniqueval)    
    
    
log = open("stacklayer.txt", "w")       
#for i in range(len(value)):
val = [455,457,458,460]
for i in range(len(val)):
   zonevalue = val[i]
   xmax = float(max(xnumber[zonevalue]))
   xmin = float(min(xnumber[zonevalue]))
   ymax = float(max(ynumber[zonevalue]))
   ymin = float(min(ynumber[zonevalue]))
   zmax = float(max(znumber[zonevalue]))
   zmin = float(min(znumber[zonevalue]))
 
   l1 = [xmin, ymax]
   r1 = [xmax, ymin]
#   for j in range(i+1,len(value)): 
   for j in range(len(zoneuniqueval)):          
      zonevalue1 = zoneuniqueval[j]
      xmax1 = float(max(xnumber[zonevalue1]))
      xmin1 = float(min(xnumber[zonevalue1]))
      ymax1 = float(max(ynumber[zonevalue1]))
      ymin1 = float(min(ynumber[zonevalue1]))
      zmax1 = float(max(znumber[zonevalue1]))
      zmin1 = float(min(znumber[zonevalue1]))
      l2 = [xmin1, ymax1]
      r2 = [xmax1, ymin1]
      if rectoverlap(xmin,xmax,ymin,ymax,zmin,zmax,xmin1,xmax1,ymin1,ymax1,zmin1,zmax1) and (zonevalue1 not in val):
          print('zone '+ str(zonevalue) + ' intersect with zone ' + str(zonevalue1), file =log) 
      x_add = abs(xmin+xmax-xmin1-xmax1)
      y_add = abs(ymax+ymin-ymax1-ymin1)
      x_sub = abs(xmax-xmin+xmax1-xmin1)
      y_sub = abs(ymax-ymin+ymax1-ymin1)
      z_add = abs(zmin+zmax-zmin1-zmax1)
      z_sub = abs(zmax-zmin+zmax1-zmin1)
      
#      if (xmin <= xmax1 and xmax >= xmin1) and (ymin <= ymax1 and ymax >= ymin1) and (zmin <= zmax1 and zmax >= zmin1) :
#          print(str(zonevalue) +'\t '+str(zonevalue1)+'\n', file =log)
      
#      if (zonevalue != zonevalue1) and (x_add <= x_sub) and (y_add <=y_sub) and (z_add <= z_sub):
#          print(str(zonevalue) +'\t '+str(zonevalue1)+'\n', file =log)
          
          
#      if ((l1[0] > r2[0]) or (l2[0] > r1[0]) or (l1[1] > r2[1]) or (l2[1] > r1[1])):
#                print('zone '+ str(zonevalue) + ' intersect with zone ' + str(zonevalue1), file =log)   
             
log.close()    


def ontop(xmin,xmax,ymin,ymax,zmin,zmax,xmin1,xmax1,ymin1,ymax1,zmin1,zmax1):
    return ((xmin == xmin1) and (xmax == xmax1) and (ymin == ymin1) and (xmax == xmax1) )


def printval(zonevalue):
   xmax = float(max(xnumber[zonevalue]))
   xmin = float(min(xnumber[zonevalue]))
   ymax = float(max(ynumber[zonevalue]))
   ymin = float(min(ynumber[zonevalue]))
   zmax = float(max(znumber[zonevalue]))
   zmin = float(min(znumber[zonevalue]))
   x = [xmin,xmax,xmax,xmin,xmin]
   y= [ymin,ymin,ymax,ymax,ymin]
   z=[zmin,zmin,zmin,zmin,zmin]
   return x,y,z
printval(455)   
   


log1 = open("overlappingnw.txt","w")
for i in range(len(value)):
   zonevalue = value[i]
   xmax = float(max(xnumber[zonevalue]))
   xmin = float(min(xnumber[zonevalue]))
   ymax = float(max(ynumber[zonevalue]))
   ymin = float(min(ynumber[zonevalue]))
   zmax = float(max(znumber[zonevalue]))
   zmin = float(min(znumber[zonevalue]))
   
   
   l1 = [xmin, ymax]
   r1 = [xmax, ymin]
   for j in range(i+1,len(value)):           
      zonevalue1 = value[j]
      xmax1 = float(max(xnumber[zonevalue1]))
      xmin1 = float(min(xnumber[zonevalue1]))
      ymax1 = float(max(ynumber[zonevalue1]))
      ymin1 = float(min(ynumber[zonevalue1]))
      zmax1 = float(max(znumber[zonevalue1]))
      zmin1 = float(min(znumber[zonevalue1]))
      
      l2 = [xmin1, ymax1]
      r2 = [xmax1, ymin1]
      if ontop(xmin,xmax,ymin,ymax,zmin,zmax,xmin1,xmax1,ymin1,ymax1,zmin1,zmax1):
          print('zone'+ str(zonevalue) + ' overlaps with zone ' + str(zonevalue1), file =log1)

      
log1.close()      


plane = pd.read_csv("bodyinfo.csv")

          
        
         
    
    
    
    
        
        
    
    

