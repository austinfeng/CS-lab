#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:30:37 2020

@author: Feng
"""
import os
#smooth: take averages. Currently discards the first few points.
path="no outliers/"
path2="no outliers/weighted averages/"
#print(os.listdir(path))
for filename in os.listdir(path):
    newfile = open(path2+"weighted "+filename,"w")
    file = open(path+filename)
    listofstuff=[]
    for line in file:
        if not line=="\n":
            listofstuff.append(line.split(","))
    newlist=[]
    for lx in range (2, len(listofstuff)-2):
        time=listofstuff[lx][0]
        value = float(listofstuff[lx-2][1])+float(listofstuff[lx-1][1])+float(listofstuff[lx][1])+float(listofstuff[lx+1][1])+float(listofstuff[lx+2][1])
        value = value/5.0
        newlist.append([time, value])
    
    print(newlist)
    for item in newlist:
        newfile.write(str(item[0])+","+str(item[1])+"\n")
