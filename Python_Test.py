# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:12:59 2017

@author: Kaustav
"""

#Question - 5
f=open("myfile.txt","w")
f.write("My favorite language for maintainability is Python.\n")
f.write("It has simple, clean syntax.\n")
f.write("It has good library support.\n")
f.close()

f2=open("myfile.txt","r+")
for line in f2:
    line=line.strip("\n")
    print(line)
f2.close()

#Question - 4
import matplotlib.pyplot as plt
age = [10,20,30,40]
weight = [22,43,54,67]
plt.scatter(age,weight)

x="Age"
y="Weight"
t="Age vs. Weight"
plt.xlabel(int(x))
plt.ylabel(int(y))
plt.title(int(t))

plt.show()

#Question - 3
number=int(input("Choose a number between 0 and 10:"))
if(number==0):
    print("You chose zero!")
elif(number==1):
    print("You chose one!")
elif(number==2):
    print("You chose two!")
elif(number==3):
    print("You chose three!")
elif(number==4):
    print("You chose four!")
elif(number==5):
    print("You chose five!")
elif(number==6):
    print("You chose six!")
elif(number==7):
    print("You chose seven!")
elif(number==8):
    print("You chose eight!")
elif(number==9):
    print("You chose nine!")
elif(number==10):
    print("You chose ten!")
else:
    print("Invalid number")
    
#Question - 1    
colors=eval(input("Enter list of colors"))  
print(colors[0])
print(colors[-1])
    
#Question - 2
data=eval(input("Enter list of numbers"))
def median(data):
    data1=sorted(data)
    n=len(data1)
    if(n%2==0):
        median=(data1[int(n/2)]+data1[int((n/2)-1)])/2
    else:
        median=data1[int((n-1)/2)]
    return median
    

median1 = median(data)
print(median1)
   
    
    
    
    
    
    
    
    
    
    
    
    