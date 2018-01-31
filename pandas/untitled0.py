# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:26:29 2018

@author: KAUSTAV
"""

import numpy
numpy.__version__
import pandas
pandas.__version__
import pandas as pd

data = pd.Series([0.25,0.5,0.75,1.0])

data.values

data=pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
data

data['b']

data=pd.Series([0.25,0.5,0.75,1.0],index=[2,5,3,7])
data
data[5]

population_dict = {'Delhi':1,
                   'Kolkata':2,
                   'Noida':3,
                   'Mumbai':4,
                   'Guwahati':5}

population_dict['California']
population_dict['California':'Illinois']

pd.Series(5, index=[100,200,300])

pd.Series({2:'a',1:'b',3:'c'},index=[3,2])


population=[100,200,300]
area=[10,20,30]
pd.DataFrame({'population':population,'area':area})

pd.DataFrame(population, columns=['population'])

rollno = [1,2,3]
names = ['A','B','C']
df1=pd.DataFrame(rollno,names,)

sdata2 = pd.DataFrame(list(zip(rollno,names)))

pd.DataFrame(np.random.rand(3,2),columns=['foo','bar'],index=['a','b','c'])

pd.index([2,3,5,7,11])

indA = pd.Index([1,3,5,7,9])
indB = pd.Index([2,3,5,7,11])
indA & indB
indA|indB

data.iloc[1]

data.iloc[1:3]

data['area']
data.area

data.area is data['area']

data.T

data.values[0]







