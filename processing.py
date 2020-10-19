#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:53:28 2020

@author: Feng
"""
import math
import os
d =dict()
#print(d)
for file in os.listdir("Lightcurve csv/csv curves"):
    if file.__contains__(".csv") and file.__contains__("edited"):
        
        #print(file[8:17])
        kid = file[15:24]
        kid2 = file[15:45]
        #if not d.__contains__(kid):
        out = open(kid2+"adj.csv","w")
        #    d.update({kid:open("full"+kid+".csv",'w')})
        openedfile = open("Lightcurve csv/csv curves/"+file)
        summ, total = [0,0]
        for line in openedfile:
            total += 1
            summ+=float(line.split(",")[1])
        #print(summ/total)
        mean = summ/total
        openedfile = open("Lightcurve csv/csv curves/"+file)#second time
        list1=[]
        dev = 0
        for line in openedfile:
            #print(line)
            dev += (float(line.split(",")[1])-mean)**2
        dev=math.sqrt(dev/total)
        openedfile = open("Lightcurve csv/csv curves/"+file)#third time
        for line in openedfile:
            value = float(line.split(",")[1])
            score = (value-mean)/dev
            if score>4:
                if score>10:
                    print(score)
            else:
                list1.append((line.split(",")[0],line.split(",")[1]))
        for item in list1:
            out.write(item[0]+","+item[1]+"\n")
        