# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:35:09 2017

@author: Kaustav
"""

data1 = [49.,66,24,98,37,64,98,27,56,93,68,78,22,25,11]

def mean(data):
    n=len(data)
    mean=sum(data)/n
    return mean

mean1 = mean(data1)
print(mean1)

data1=[1,2,5,10,-20,30]
def median(data):
    data1=sorted(data)
    n=len(data1)
    if(n%2==0):
        median=(data1[int(n/2)]+data1[int((n/2)-1)])/2
    else:
        median=data1[int((n-1)/2)]
    return median
    

median1 = median(data1)
print(median1)

data1=[1,2,5,10,-20,5,5]

import statistics as s
data1 = [49.,66,24,98,37,66,98,27,56,93,66,78,22,22,11]
mode=s.mode(data1)
print(mode) 


import statistics as s
data1 = [49.,66,24,98,37,66,98,27,56,93,66,78,22,22,11]
v=s.variance(data1)
print(v) 

import statistics as s
data1 = [49.,66,24,98,37,66,98,27,56,93,66,78,22,22,11]
st=round(s.stdev(data1))
print(st) 
