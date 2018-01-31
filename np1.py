# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:27:40 2018

@author: KAUSTAV
"""

import numpy
numpy.__version__
numpy.abs

import array
L=list(range(10))
A=array.array('i',L)
A

import numpy as np
np.array([1,4,2,5,3])

np.array([3.14,4,2,3])

np.array([1,2,3,4],dtype='float32')

np.array([range(i,i+3) for i in [2,4,6]])

np.zeros(10,dtype=int)

np.ones((3,5), dtype=float)

np.full((3,5),3.14)

np.full(shape=(3,5), fill_value=3.14, dtype=None)

npm = np.arange(0,20,2)

np.linspace(0,1,5)

len(npm)

np.random.random((3,3))

np.random.normal(0,1,(3,3))

np.random.randint(0,10,(3,3))

np.eye(3)

np.empty(3)

import numpy as np
np.random.seed(0)

x1=np.random.randint(10, size=6)
x2=np.random.randint(10, size=(3,4))
x3=np.random.randint(10, size=(3,4,5))

x1
x2
x3

print("x3 ndim: ",x3.ndim)
print("x3 shape:",x3.shape)
print("x3 size: ",x3.size)

print("itemsize:",x3.itemsize,"bytes")
print("nbytes:",x3.nbytes,"bytes")

x1[-1]

x2[0,0]

x2[2,1]

x2[0,0]=12

x2

x1[0]=3.14159
x1

x=np.arange(10)
x

x[:5]
x[5:]

x[4:7]

x[::2]

x[1::2]

x[::-1]

x[5::-2]

x2

x2[:2,:3]

x2[:3,::2]

x2[::-1,::-1]
x2

print(x2[:,0])

print(x2[0,:])

print(x2[0])

x2_sub=x2[:2,:2]
print(x2_sub)

x2_sub[0,0] = 99
print(x2_sub)

print(x2)

x2_sub_copy = x2[:2,:2].copy()
print(x2_sub_copy)

x2_sub_copy[0,0]=42
print(x2_sub_copy)

print(x2)




