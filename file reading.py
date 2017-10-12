# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:06:06 2017

@author: Kaustav
"""

str = input("Enter your input:" )
print("Received input is : ",str)

str=eval(input("Enter your input:" ))
print("Received input is : ",str)

import os
os.getcwd()
os.listdir()
os.listdir("E:\\")
os.mkdir("E:\\test")
os.chdir("E:\\test")
os.getcwd()
os.chdir("..")
os.getcwd()
os.rmdir("E:\\test")
f = open("E:\\pyWork\\pyProjects\\Py_in_Action\\abc.txt")
f.close()
os.rename("abc.txt","def.txt")
fo=open("foo.txt","w")
fo.write("Python is a great language.\r\nYeah its great!!\r\n")
fo.close()
fo=open("foo.txt","r+")
str=fo.read(20)
print(str)
position=fo.tell()
print(position)
position=fo.seek(3,0)
print(position)

f=open("sunday.txt","w")
f.write("Today is Sunday\n")
f.write("Sunday\n")
f.write("Today is first Sunday\n")
f.write("first Sunday")
f.close()

def input_stats(filename):
    input=open(filename)
    longest=""
    for line in input:
        if len(line) > len(longest):
            longest=line
    
    print("Longest Line =", len(longest))
    print(longest)

input_stats("sunday.txt")

fo=open("sunday.txt","r+")
for line in fo:
    line=line.strip("\n")
    print(line)
fo.close()