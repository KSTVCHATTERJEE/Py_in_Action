# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:11:10 2018

@author: KAUSTAV
"""

L = eval(input("Enter a list"))

rollnos = [1,2,3,4,5,6,10,11,14]
rollnos[0]
rollnos[8]
len(rollnos)
sum(rollnos)
max(rollnos)
min(rollnos)
rollnos

for i in range(len(rollnos)):
    print(rollnos[i], end=',')

if 3 in rollnos:
    print('Yes')

if 13 in rollnos:
    print('Yes')
else:
    print('No')

rollnos.append(13)
rollnos

sorted(rollnos)

rollnos.index(13)



