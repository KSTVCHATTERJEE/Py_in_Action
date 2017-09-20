# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:16:53 2017

@author: Kaustav
"""

x=int(input("Enter value of x "))
if (x==3):
    print ("X equals 3")
elif (x==2):
    print ("X equals 2")
else:
    print ("X equals something else")
print ("This is outside the if")

for someChar in "Hello World":
    print(someChar)
    
for i in ['P','Y','T','H','O','N']:
    print(i)
    
for (x,y) in [('a',1),('b',2),('c',3),('d',4)]:
    print (x)

weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(weekdays)
for weekday in weekdays:
    print (weekday)
    
for x in range(15):
    print(x)

numbers=[1,2,3,4,5,6]
for x in numbers:
    if x in [2,3,4,5]:
        x+=5
    print(x)
    
numbers = [1,2,3,4,5,6]
for x in numbers:
    if (x%2==0):
        x+=5
    print(x)
  
x=3
while x<10:
    x+=1
    print("Still in the loop")
print("Outside of the loop")
  
while 1:
    print("Type Ctrl-C to stop me!")
    
x="spam"
while x:
    print (x)
    x=x[1:]
    
while 1:
    name=input('Enter name:')
    if name =='stop':
        break
    age=input('Enter age:')
    print('Hello',name,"=>",int(age)**2)
    
x=10
while x:
    x-=1
    if (x%2!=0):
        continue
    print(x)
    

x=10
while x:
    x-=1
    if (x%2==0):
        continue
    print(x)
    
def myfun(b,c):
    return b+c
myfun(3,4)

def hello():
    name=str(input("Enter your name: "))
    if name:
        print("Hello"+str(name))
    else:
        print("Hello World")
    return

hello()