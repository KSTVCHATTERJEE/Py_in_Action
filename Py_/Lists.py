# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:34:45 2017

@author: Administrator
"""

fam = [1.73,1.68,1.71,1.89]
print(fam)
print(fam+fam)
print(fam*3)
fam = ["liz",1.73,"emma",1.68,"mom",1.71,"dad",1.89]
print(fam)
type(fam)
fam[3]
fam[6]
fam[10]
fam[-1]
fam[-2]
fam[3:5]
fam[1:4]
fam[:4]
fam[5:]
fam[1]=1.86
print(fam)
fam[0:2]=["lisa",1.74]
fam_ext = fam + ["me",1.79]
print(fam_ext)
del(fam[2])
print(fam)
x = ['a','b','c']
y=x
print(y[1])
y[1]='z'
print(y)
print(x)
y=list(x)
print(y)
y=x[:]
y[1]="z"
print(y)
print(x)