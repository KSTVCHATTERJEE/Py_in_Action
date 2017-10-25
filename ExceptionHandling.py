# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:41:21 2017

@author: Kaustav
"""

try:
    fh = open("testfile.txt","w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can't find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()
    