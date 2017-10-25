# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:57:59 2017

@author: Kaustav
"""

import time
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:",ticks)

import time;
localtime=time.localtime(time.time())
print("Local current time :",localtime)

import time;
localtime = time.asctime(time.localtime(time.time()))
print("Local current time :",localtime)

import calendar

cal=calendar.month(2017,5)
print("Here is the calendar:")
print(cal)

import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print("Yesterday",yesterday)
print("Today",today)
print("Tomorrow",tomorrow)

from datetime import date
a = date(2016,1,31)
b = date(2017,1,31)
print(b-a)