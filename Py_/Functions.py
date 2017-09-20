# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:13:28 2017

@author: Kaustav
"""

fam = [1.73,1.68,1.71,1.89]
fam
max(fam)
tallest = max(fam)
tallest
round(1.68,1)
help(round)
sister="liz"
sister.replace('z','sa')
fam.append("me")
fam
import numpy as np
np.array([1,2,3])
height=[1,2,3,4,5]
weight=[20,30,40,50,60]
weight/height**2

np_height=np.array(height)
np_weight=np.array(weight)
np_weight/np_height**2

python_list=[1,2,3]
numpy_array=np.array([1,2,3])
python_list+python_list
numpy_array+numpy_array

bmi=np.array([1,2,3,4,5])
bmi
bmi[1]
bmi>4
bmi[bmi>4]
type(np_height)