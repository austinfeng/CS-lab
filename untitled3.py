#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:07:39 2020

@author: Feng
"""
import os
file=open("cumulative_2020.09.11_05.40.08.csv")
d =dict()
for line in file:
    #print(line)
    splitted = line.split(",")
    #print(splitted)
    if len(splitted)>13:
        d.update({splitted[0]:(splitted[10],splitted[13])})
print(d)
for file in os.listdir("Lightcurve csv/csv curves"):
    if file.__contains__(".csv") and not file.__contains__("edited"):
        #print(file[8:17])
        t = file[8:17]
        t=str(int(str(t)))
        print(t)
        x=d.get(t)
        openedfile = open("Lightcurve csv/csv curves/"+file)
        string = ""
        for line in openedfile:
            if not(line.split(",")[1].replace("\n","")=="-9.900000e+01"):
                start=float(x[1])
                pd = float(x[0])
                value = float(line.split(",")[0])
                newvalue = (value-(start-pd/2.0))%pd
                string += str(newvalue)+","+line.split(",")[1]
        print(string)
        openedfile = open("Lightcurve csv/csv curves/edited_"+file,"w")
        openedfile.write(string)