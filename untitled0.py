#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:12:23 2020

@author: Feng
"""
def convertto99s(i):
    j = list(i)
    for x in range (0,len(j)):
        #print(j[x])
        if j[x]!=j[x]:
            j[x]=-99
            #print("d")
    return tuple(j)
from os import listdir
import numpy
from astropy.io import fits
#print(listdir())
# ask for an input file 
for f in listdir():
    if f.__contains__(".fits"):
        filename = f
        print(filename)
        # ask for an output file name
        output = f[:-5]+".csv"
        
        # Open the given fits file
        hdulist = fits.open(filename)
        
        scidata = hdulist[1].data
        for i in range (0,len(scidata)):
            scidata[i] = convertto99s(scidata[i])
        print(scidata)
            #print(scidata[i])
        # save your new file as a csv
        numpy.savetxt(output, scidata, fmt='%e', delimiter=',')
