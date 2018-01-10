# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:06:15 2017

@author: kgavini
"""


def zoneintersection():
    import pandas as pd


    # import files and preprocessing
    df = pd.read_csv("points.csv") 
    df1 = pd.read_csv("verts.csv", header = 0)
    xaxis = df.loc[:,'x']
    yaxis = df.loc[:,'y']
    zaxis = df.loc[:,'z']
    index = df.loc[:,'index']
    position1index = df1.loc[:,'position1']
    position2index = df1.loc[:,'position2']
    position3index = df1.loc[:,'position3']


    # filter x and y axis from first data set and append it into second one       
    x1 = [df.loc[(position1index[i])-1,'xaxis'] for i in range(len(position1index)) ]
    df1['x1'] = pd.Series(x1, index=df1.index)
    y1 = [df.loc[(position1index[i])-1,'yaxis'] for i in range(len(position1index)) ]
    df1['y1'] = pd.Series(y1, index=df1.index)
    x2 = [df.loc[(position2index[i])-1,'xaxis'] for i in range(len(position2index)) ]
    df1['x2'] = pd.Series(x2, index=df1.index)
    y2 = [df.loc[(position2index[i])-1,'yaxis'] for i in range(len(position2index)) ]
    df1['y2'] = pd.Series(y2, index=df1.index)
    x3 = [df.loc[(position3index[i])-1,'xaxis'] for i in range(len(position3index)) ]
    df1['x3'] = pd.Series(x3, index=df1.index)
    y3 = [df.loc[(position3index[i])-1,'yaxis'] for i in range(len(position3index)) ]
    df1['y3'] = pd.Series(y3, index=df1.index)

    # remove unwanted columns 
    cols = df1.columns.tolist()
    cols1 = cols[6:12] +cols[4:5]
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
           
           
    # find intersection between different zones           
    value = [1837 ,1747]

    #loop through every possible zone pair and find the intersection  
    log = open("zoneinfo.txt", "w")       
    for i in range(len(value)):
        zonevalue = list(value)[i]
        xmax = max(xnumber[zonevalue])
        xmin = min(xnumber[zonevalue])
        ymax = max(ynumber[zonevalue])
        ymin = min(ynumber[zonevalue])
        l1 = [xmin, ymax]
        r1 = [xmax, ymin]
        for j in range(i+1,len(value)):           
            zonevalue1 = list(value)[j]
            xmax1 = max(xnumber[zonevalue])
            xmin1 = min(xnumber[zonevalue])
            ymax1 = max(ynumber[zonevalue])
            ymin1 = min(ynumber[zonevalue])
            l2 = [xmin1, ymax1]
            r2 = [xmax1, ymin1]
            if not ((l1[0] > r2[0]) or (l2[0] > r1[0]) or (l1[1] > r2[1]) or (l2[1] > r1[1])):
                print('zone '+ str(zonevalue) + ' intersect with zone ' + str(zonevalue1), file =log)
            else: print('nothing happening', file =log)    
             
    log.close()        
    return None


zoneintersection()        
            
        
         
    
    
    
    
        
        
    
    

