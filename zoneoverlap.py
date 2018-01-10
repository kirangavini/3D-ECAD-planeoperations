# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:39:54 2017

@author: kgavini
"""
import pandas as pd
plane = pd.read_csv("bodyinfo_d8_small.csv")

xval_max = []
xval_min = []
yval_max = []
yval_min = []
zval_max = []
zval_min = []

for index_val in range(len(plane)):
    
    if plane.loc[index_val].count() == 2:
        zone = plane.loc[index_val,'Zone1']
     
       
        xval_max.append(max(xnumber[zone]))
        xval_min.append(min(xnumber[zone]))
        yval_max.append(max(ynumber[zone]))
        yval_min.append(min(ynumber[zone]))
        zval_max.append(max(znumber[zone]))
        zval_min.append(min(znumber[zone]))
    elif plane.loc[index_val].count() == 6: 
        zone1 = [int(plane.loc[index_val,'Zone1']), int(plane.loc[index_val,'Zone2']), int(plane.loc[index_val,'Zone3']), int(plane.loc[index_val,'Zone4']), int(plane.loc[index_val,'Zone5']) ]
        xvalmx = []
        xvalmn = []
        yvalmx = []
        yvalmn = []
        zvalmx = []
        zvalmn = []
        
        for i in zone1:
            xvalmx.append(max(xnumber[i]))
            xvalmn.append(min(xnumber[i]))
            yvalmx.append(max(ynumber[i]))
            yvalmn.append(min(ynumber[i]))
            zvalmx.append(max(znumber[i]))
            zvalmn.append(min(znumber[i]))
              
        xval_max.append(max(xvalmx))
        xval_min.append(min(xvalmn))
        yval_max.append(max(yvalmx))
        yval_min.append(min(yvalmn))
        zval_max.append(max(zvalmx))
        zval_min.append(min(zvalmn))    
        
        
        
        
        
    elif plane.loc[index_val].count() == 7: 
        zone1 = [int(plane.loc[index_val,'Zone1']), int(plane.loc[index_val,'Zone2']), int(plane.loc[index_val,'Zone3']), int(plane.loc[index_val,'Zone4']), int(plane.loc[index_val,'Zone5']), int(plane.loc[index_val,'Zone6']) ]
        xvalmx = []
        xvalmn = []
        yvalmx = []
        yvalmn = []
        zvalmx = []
        zvalmn = []
        
        for i in zone1:
            xvalmx.append(max(xnumber[i]))
            xvalmn.append(min(xnumber[i]))
            yvalmx.append(max(ynumber[i]))
            yvalmn.append(min(ynumber[i]))
            zvalmx.append(max(znumber[i]))
            zvalmn.append(min(znumber[i]))
              
        xval_max.append(max(xvalmx))
        xval_min.append(min(xvalmn))
        yval_max.append(max(yvalmx))
        yval_min.append(min(yvalmn))
        zval_max.append(max(zvalmx))
        zval_min.append(min(zvalmn))
        
    elif plane.loc[index_val].count() == 9: 
        zone1 = [int(plane.loc[index_val,'Zone1']), int(plane.loc[index_val,'Zone2']), int(plane.loc[index_val,'Zone3']), int(plane.loc[index_val,'Zone4']), int(plane.loc[index_val,'Zone5']), int(plane.loc[index_val,'Zone6']),int(plane.loc[index_val,'Zone7']),int(plane.loc[index_val,'Zone8']) ]
        xvalmx = []
        xvalmn = []
        yvalmx = []
        yvalmn = []
        zvalmx = []
        zvalmn = []
        
        for i in zone1:
            xvalmx.append(max(xnumber[i]))
            xvalmn.append(min(xnumber[i]))
            yvalmx.append(max(ynumber[i]))
            yvalmn.append(min(ynumber[i]))
            zvalmx.append(max(znumber[i]))
            zvalmn.append(min(znumber[i]))
              
        xval_max.append(max(xvalmx))
        xval_min.append(min(xvalmn))
        yval_max.append(max(yvalmx))
        yval_min.append(min(yvalmn))
        zval_max.append(max(zvalmx))
        zval_min.append(min(zvalmn))    
              
              
    elif plane.loc[index_val].count() == 11: 
        zone1 = [int(plane.loc[index_val,'Zone1']), int(plane.loc[index_val,'Zone2']), int(plane.loc[index_val,'Zone3']), int(plane.loc[index_val,'Zone4']), int(plane.loc[index_val,'Zone5']), int(plane.loc[index_val,'Zone6']), int(plane.loc[index_val,'Zone7']), int(plane.loc[index_val,'Zone8']), int(plane.loc[index_val,'Zone9']), int(plane.loc[index_val,'Zone10']) ]
        xvalmx = []
        xvalmn = []
        yvalmx = []
        yvalmn = []
        zvalmx = []
        zvalmn = []
        
        for i in zone1:
            xvalmx.append(max(xnumber[i]))
            xvalmn.append(min(xnumber[i]))
            yvalmx.append(max(ynumber[i]))
            yvalmn.append(min(ynumber[i]))
            zvalmx.append(max(znumber[i]))
            zvalmn.append(min(znumber[i]))
              
        xval_max.append(max(xvalmx))
        xval_min.append(min(xvalmn))
        yval_max.append(max(yvalmx))
        yval_min.append(min(yvalmn))
        zval_max.append(max(zvalmx))
        zval_min.append(min(zvalmn))
        
    elif plane.loc[index_val].count() == 20: 
        
        zone1 = [int(plane.loc[index_val,'Zone1']),
                    int(plane.loc[index_val,'Zone2']),
                    int(plane.loc[index_val,'Zone3']),
                    int(plane.loc[index_val,'Zone4']),
                    int(plane.loc[index_val,'Zone5']),
                    int(plane.loc[index_val,'Zone6']),
                    int(plane.loc[index_val,'Zone7']),
                    int(plane.loc[index_val,'Zone8']),
                    int(plane.loc[index_val,'Zone9']),
                    int(plane.loc[index_val,'Zone10']),
                    int(plane.loc[index_val,'Zone11']),
                    int(plane.loc[index_val,'Zone12']),
                    int(plane.loc[index_val,'Zone13']),
                    int(plane.loc[index_val,'Zone14']),
                    int(plane.loc[index_val,'Zone15']),
                    int(plane.loc[index_val,'Zone16']),
                    int(plane.loc[index_val,'Zone17']),
                    int(plane.loc[index_val,'Zone18']),
                    int(plane.loc[index_val,'Zone19'])]
        xvalmn = []
        yvalmx = []
        yvalmn = []
        zvalmx = []
        zvalmn = []
        
        for i in zone1:
            xvalmx.append(max(xnumber[i]))
            xvalmn.append(min(xnumber[i]))
            yvalmx.append(max(ynumber[i]))
            yvalmn.append(min(ynumber[i]))
            zvalmx.append(max(znumber[i]))
            zvalmn.append(min(znumber[i]))
              
        xval_max.append(max(xvalmx))
        xval_min.append(min(xvalmn))
        yval_max.append(max(yvalmx))
        yval_min.append(min(yvalmn))
        zval_max.append(max(zvalmx))
        zval_min.append(min(zvalmn))
    
    elif plane.loc[index_val].count() == 22:
        
        zone1 = [int(plane.loc[index_val,'Zone1']),
                    int(plane.loc[index_val,'Zone2']),
                    int(plane.loc[index_val,'Zone3']),
                    int(plane.loc[index_val,'Zone4']),
                    int(plane.loc[index_val,'Zone5']),
                    int(plane.loc[index_val,'Zone6']),
                    int(plane.loc[index_val,'Zone7']),
                    int(plane.loc[index_val,'Zone8']),
                    int(plane.loc[index_val,'Zone9']),
                    int(plane.loc[index_val,'Zone10']),
                    int(plane.loc[index_val,'Zone11']),
                    int(plane.loc[index_val,'Zone12']),
                    int(plane.loc[index_val,'Zone13']),
                    int(plane.loc[index_val,'Zone14']),
                    int(plane.loc[index_val,'Zone15']),
                    int(plane.loc[index_val,'Zone16']),
                    int(plane.loc[index_val,'Zone17']),
                    int(plane.loc[index_val,'Zone18']),
                    int(plane.loc[index_val,'Zone19']),
                    int(plane.loc[index_val,'Zone20']),
                    int(plane.loc[index_val,'Zone21'])]
        xvalmx = []
        xvalmn = []
        yvalmx = []
        yvalmn = []
        zvalmx = []
        zvalmn = []
        
        for i in zone1:
            xvalmx.append(max(xnumber[i]))
            xvalmn.append(min(xnumber[i]))
            yvalmx.append(max(ynumber[i]))
            yvalmn.append(min(ynumber[i]))
            zvalmx.append(max(znumber[i]))
            zvalmn.append(min(znumber[i]))
              
        xval_max.append(max(xvalmx))
        xval_min.append(min(xvalmn))
        yval_max.append(max(yvalmx))
        yval_min.append(min(yvalmn))
        zval_max.append(max(zvalmx))
        zval_min.append(min(zvalmn))  
        
    elif plane.loc[index_val].count() == 35: 
     
        zone1 = [int(plane.loc[index_val,'Zone1']),
                    int(plane.loc[index_val,'Zone2']),
                    int(plane.loc[index_val,'Zone3']),
                    int(plane.loc[index_val,'Zone4']),
                    int(plane.loc[index_val,'Zone5']),
                    int(plane.loc[index_val,'Zone6']),
                    int(plane.loc[index_val,'Zone7']),
                    int(plane.loc[index_val,'Zone8']),
                    int(plane.loc[index_val,'Zone9']),
                    int(plane.loc[index_val,'Zone10']),
                    int(plane.loc[index_val,'Zone11']),
                    int(plane.loc[index_val,'Zone12']),
                    int(plane.loc[index_val,'Zone13']),
                    int(plane.loc[index_val,'Zone14']),
                    int(plane.loc[index_val,'Zone15']),
                    int(plane.loc[index_val,'Zone16']),
                    int(plane.loc[index_val,'Zone17']),
                    int(plane.loc[index_val,'Zone18']),
                    int(plane.loc[index_val,'Zone19']),
                    int(plane.loc[index_val,'Zone20']),
                    int(plane.loc[index_val,'Zone21']),
                    int(plane.loc[index_val,'Zone22']),
                    int(plane.loc[index_val,'Zone23']),
                    int(plane.loc[index_val,'Zone24']),
                    int(plane.loc[index_val,'Zone25']),
                    int(plane.loc[index_val,'Zone26']),
                    int(plane.loc[index_val,'Zone27']),
                    int(plane.loc[index_val,'Zone28']),
                    int(plane.loc[index_val,'Zone29']),
                    int(plane.loc[index_val,'Zone30']),
                    int(plane.loc[index_val,'Zone31']),
                    int(plane.loc[index_val,'Zone32']),
                    int(plane.loc[index_val,'Zone33']),
                    int(plane.loc[index_val,'Zone34'])]




        xvalmx = []
        xvalmn = []
        yvalmx = []
        yvalmn = []
        zvalmx = []
        zvalmn = []
        
        for i in zone1:
            xvalmx.append(max(xnumber[i]))
            xvalmn.append(min(xnumber[i]))
            yvalmx.append(max(ynumber[i]))
            yvalmn.append(min(ynumber[i]))
            zvalmx.append(max(znumber[i]))
            zvalmn.append(min(znumber[i]))
              
        xval_max.append(max(xvalmx))
        xval_min.append(min(xvalmn))
        yval_max.append(max(yvalmx))
        yval_min.append(min(yvalmn))
        zval_max.append(max(zvalmx))
        zval_min.append(min(zvalmn))    
        
    elif plane.loc[index_val].count() == 152: 

        zone1 = [int(plane.loc[index_val,'Zone1']),
                    int(plane.loc[index_val,'Zone2']),
                    int(plane.loc[index_val,'Zone3']),
                    int(plane.loc[index_val,'Zone4']),
                    int(plane.loc[index_val,'Zone5']),
                    int(plane.loc[index_val,'Zone6']),
                    int(plane.loc[index_val,'Zone7']),
                    int(plane.loc[index_val,'Zone8']),
                    int(plane.loc[index_val,'Zone9']),
                    int(plane.loc[index_val,'Zone10']),
                    int(plane.loc[index_val,'Zone11']),
                    int(plane.loc[index_val,'Zone12']),
                    int(plane.loc[index_val,'Zone13']),
                    int(plane.loc[index_val,'Zone14']),
                    int(plane.loc[index_val,'Zone15']),
                    int(plane.loc[index_val,'Zone16']),
                    int(plane.loc[index_val,'Zone17']),
                    int(plane.loc[index_val,'Zone18']),
                    int(plane.loc[index_val,'Zone19']),
                    int(plane.loc[index_val,'Zone20']),
                    int(plane.loc[index_val,'Zone21']),
                    int(plane.loc[index_val,'Zone22']),
                    int(plane.loc[index_val,'Zone23']),
                    int(plane.loc[index_val,'Zone24']),
                    int(plane.loc[index_val,'Zone25']),
                    int(plane.loc[index_val,'Zone26']),
                    int(plane.loc[index_val,'Zone27']),
                    int(plane.loc[index_val,'Zone28']),
                    int(plane.loc[index_val,'Zone29']),
                    int(plane.loc[index_val,'Zone30']),
                    int(plane.loc[index_val,'Zone31']),
                    int(plane.loc[index_val,'Zone32']),
                    int(plane.loc[index_val,'Zone33']),
                    int(plane.loc[index_val,'Zone34']),
                    int(plane.loc[index_val,'Zone35']),
                    int(plane.loc[index_val,'Zone36']),
                    int(plane.loc[index_val,'Zone37']),
                    int(plane.loc[index_val,'Zone38']),
                    int(plane.loc[index_val,'Zone39']),
                    int(plane.loc[index_val,'Zone40']),
                    int(plane.loc[index_val,'Zone41']),
                    int(plane.loc[index_val,'Zone42']),
                    int(plane.loc[index_val,'Zone43']),
                    int(plane.loc[index_val,'Zone44']),
                    int(plane.loc[index_val,'Zone45']),
                    int(plane.loc[index_val,'Zone46']),
                    int(plane.loc[index_val,'Zone47']),
                    int(plane.loc[index_val,'Zone48']),
                    int(plane.loc[index_val,'Zone49']),
                    int(plane.loc[index_val,'Zone50']),
                    int(plane.loc[index_val,'Zone51']),
                    int(plane.loc[index_val,'Zone52']),
                    int(plane.loc[index_val,'Zone53']),
                    int(plane.loc[index_val,'Zone54']),
                    int(plane.loc[index_val,'Zone55']),
                    int(plane.loc[index_val,'Zone56']),
                    int(plane.loc[index_val,'Zone57']),
                    int(plane.loc[index_val,'Zone58']),
                    int(plane.loc[index_val,'Zone59']),
                    int(plane.loc[index_val,'Zone60']),
                    int(plane.loc[index_val,'Zone61']),
                    int(plane.loc[index_val,'Zone62']),
                    int(plane.loc[index_val,'Zone63']),
                    int(plane.loc[index_val,'Zone64']),
                    int(plane.loc[index_val,'Zone65']),
                    int(plane.loc[index_val,'Zone66']),
                    int(plane.loc[index_val,'Zone67']),
                    int(plane.loc[index_val,'Zone68']),
                    int(plane.loc[index_val,'Zone69']),
                    int(plane.loc[index_val,'Zone70']),
                    int(plane.loc[index_val,'Zone71']),
                    int(plane.loc[index_val,'Zone72']),
                    int(plane.loc[index_val,'Zone73']),
                    int(plane.loc[index_val,'Zone74']),
                    int(plane.loc[index_val,'Zone75']),
                    int(plane.loc[index_val,'Zone76']),
                    int(plane.loc[index_val,'Zone77']),
                    int(plane.loc[index_val,'Zone78']),
                    int(plane.loc[index_val,'Zone79']),
                    int(plane.loc[index_val,'Zone80']),
                    int(plane.loc[index_val,'Zone81']),
                    int(plane.loc[index_val,'Zone82']),
                    int(plane.loc[index_val,'Zone83']),
                    int(plane.loc[index_val,'Zone84']),
                    int(plane.loc[index_val,'Zone85']),
                    int(plane.loc[index_val,'Zone86']),
                    int(plane.loc[index_val,'Zone87']),
                    int(plane.loc[index_val,'Zone88']),
                    int(plane.loc[index_val,'Zone89']),
                    int(plane.loc[index_val,'Zone90']),
                    int(plane.loc[index_val,'Zone91']),
                    int(plane.loc[index_val,'Zone92']),
                    int(plane.loc[index_val,'Zone93']),
                    int(plane.loc[index_val,'Zone94']),
                    int(plane.loc[index_val,'Zone95']),
                    int(plane.loc[index_val,'Zone96']),
                    int(plane.loc[index_val,'Zone97']),
                    int(plane.loc[index_val,'Zone98']),
                    int(plane.loc[index_val,'Zone99']),
                    int(plane.loc[index_val,'Zone100']),
                    int(plane.loc[index_val,'Zone101']),
                    int(plane.loc[index_val,'Zone102']),
                    int(plane.loc[index_val,'Zone103']),
                    int(plane.loc[index_val,'Zone104']),
                    int(plane.loc[index_val,'Zone105']),
                    int(plane.loc[index_val,'Zone106']),
                    int(plane.loc[index_val,'Zone107']),
                    int(plane.loc[index_val,'Zone108']),
                    int(plane.loc[index_val,'Zone109']),
                    int(plane.loc[index_val,'Zone110']),
                    int(plane.loc[index_val,'Zone111']),
                    int(plane.loc[index_val,'Zone112']),
                    int(plane.loc[index_val,'Zone113']),
                    int(plane.loc[index_val,'Zone114']),
                    int(plane.loc[index_val,'Zone115']),
                    int(plane.loc[index_val,'Zone116']),
                    int(plane.loc[index_val,'Zone117']),
                    int(plane.loc[index_val,'Zone118']),
                    int(plane.loc[index_val,'Zone119']),
                    int(plane.loc[index_val,'Zone120']),
                    int(plane.loc[index_val,'Zone121']),
                    int(plane.loc[index_val,'Zone122']),
                    int(plane.loc[index_val,'Zone123']),
                    int(plane.loc[index_val,'Zone124']),
                    int(plane.loc[index_val,'Zone125']),
                    int(plane.loc[index_val,'Zone126']),
                    int(plane.loc[index_val,'Zone127']),
                    int(plane.loc[index_val,'Zone128']),
                    int(plane.loc[index_val,'Zone129']),
                    int(plane.loc[index_val,'Zone130']),
                    int(plane.loc[index_val,'Zone131']),
                    int(plane.loc[index_val,'Zone132']),
                    int(plane.loc[index_val,'Zone133']),
                    int(plane.loc[index_val,'Zone134']),
                    int(plane.loc[index_val,'Zone135']),
                    int(plane.loc[index_val,'Zone136']),
                    int(plane.loc[index_val,'Zone137']),
                    int(plane.loc[index_val,'Zone138']),
                    int(plane.loc[index_val,'Zone139']),
                    int(plane.loc[index_val,'Zone140']),
                    int(plane.loc[index_val,'Zone141']),
                    int(plane.loc[index_val,'Zone142']),
                    int(plane.loc[index_val,'Zone143']),
                    int(plane.loc[index_val,'Zone144']),
                    int(plane.loc[index_val,'Zone145']),
                    int(plane.loc[index_val,'Zone146']),
                    int(plane.loc[index_val,'Zone147']),
                    int(plane.loc[index_val,'Zone148']),
                    int(plane.loc[index_val,'Zone149']),
                    int(plane.loc[index_val,'Zone150']),
                    int(plane.loc[index_val,'Zone151'])]














        xvalmx = []
        xvalmn = []
        yvalmx = []
        yvalmn = []
        zvalmx = []
        zvalmn = []
        
        for i in zone1:
            xvalmx.append(max(xnumber[i]))
            xvalmn.append(min(xnumber[i]))
            yvalmx.append(max(ynumber[i]))
            yvalmn.append(min(ynumber[i]))
            zvalmx.append(max(znumber[i]))
            zvalmn.append(min(znumber[i]))
              
        xval_max.append(max(xvalmx))
        xval_min.append(min(xvalmn))
        yval_max.append(max(yvalmx))
        yval_min.append(min(yvalmn))
        zval_max.append(max(zvalmx))
        zval_min.append(min(zvalmn))    
        


plane['xmax'] = pd.Series(xval_max, index=plane.index)   
plane['xmin'] = pd.Series(xval_min, index=plane.index)
plane['ymax'] = pd.Series(yval_max, index=plane.index) 
plane['ymin'] = pd.Series(yval_min, index=plane.index) 
plane['zmax'] = pd.Series(zval_max, index=plane.index)
plane['zmin'] = pd.Series(zval_min, index=plane.index) 


def ontop(xmin,xmax,ymin,ymax,zmin,zmax,xmin1,xmax1,ymin1,ymax1,zmin1,zmax1):
    return ((xmin == xmin1) and (xmax == xmax1) and (ymin == ymin1) and (xmax == xmax1) and (zmin == zmin1) and (zmax == zmax1 ))


log1 = open("zoneoverlap.txt","w")
mul = []
for i in range(len(plane)):
   xmax = float(plane.loc[i,'xmax'])
   xmin = float(plane.loc[i,'xmin'])
   ymax = float(plane.loc[i,'ymax'])
   ymin = float(plane.loc[i,'ymin'])
   zmax = float(plane.loc[i,'zmax'])
   zmin = float(plane.loc[i,'zmin'])
   
   for j in range(i,len(plane)):           
      xmax1 = float(plane.loc[j,'xmax'])
      xmin1 = float(plane.loc[j,'xmin'])
      ymax1 = float(plane.loc[j,'ymax'])
      ymin1 = float(plane.loc[j,'ymin'])
      zmax1 = float(plane.loc[j,'zmax'])
      zmin1 = float(plane.loc[j,'zmin'])
      
      
      if (i != j) and ontop(xmin,xmax,ymin,ymax,zmin,zmax,xmin1,xmax1,ymin1,ymax1,zmin1,zmax1):
            print('zone '+ str(plane.loc[i,'Body']) + ' duplicates with ' + str(plane.loc[j,'Body']), file =log1)

log1.close()      


      
            
            
            
            
        
       
        
        
        
        
        
        