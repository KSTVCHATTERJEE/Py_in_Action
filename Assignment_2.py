# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:10:31 2017

@author: Kaustav
"""


def lone_sum(a,b,c):
    if ((a!=b)&(b!=c)&(c!=a)):
        result=a+b+c
    if((a==b)|(b==c)|(c==a)):
        result=c
    if((a==b)&(b==c)&(c==a)):
        result=0
    return result   
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
result=lone_sum(a,b,c)
print(result)

def close_far(a, b, c):
    abs_a = abs(b-a)
    abs_b = abs(c-a)
    abs_c = abs(c-b)
    if abs_b <= 1 and abs_b >= 2 and abs_c >= 2
        res=True
    elif abs_c <= 1 and abs_a >= 2 and abs_c >= 2:
        res=True
    else:
        res=False
    return res
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
result


def counthi(str):
    result = str.count("hi")
    return result
str = input("Enter string")
r1 = counthi(str)
print(r1)



res = "Hello World"
res1=res[::-1]
print(res1)
?casefold

str=input("Enter word")
str1=str[::-1]
print(str1)

def leap(year):
    if((year%100!=0)&(year%4==0)):
        print(year,"is a leap year")
    elif((year%100==0)&(year%400==0)):
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")

year=int(input("Enter a year"))
leap(year)   
