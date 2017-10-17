# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:36:41 2017

@author: Kaustav
"""

name="Brave Sir Robin"
for word in name.split():
    print(word)
    
print(name.split("r"))

"LL".join(name.split("r"))

s= "Jessica 31 647.28"
name,age,money=s.split()
print(name)
print(int(age))
print(float(money))

f=open("hours.txt","w")
f.write("123 Suzy 9.5 8.1 7.6 3.1 3.2\n")
f.write("456 Brad 7.0 9.6 6.5 4.9 8.8\n")
f.write("789 Jenn 8.0 8.0 8.0 8.0 8.1\n")
f.close()

fo=open("hours.txt","r+")
for line in fo:
    line=line.strip("\n")
    ID,name,Mon,Tue,Wed,Thu,Fri=line.split()
    sum=float(Mon)+float(Tue)+float(Wed)+float(Thu)+float(Fri)
    avg=sum/5
    print(name,"ID",ID,"worked",round(sum,1),"hours:",round(avg,1),"/day")
fo.close()