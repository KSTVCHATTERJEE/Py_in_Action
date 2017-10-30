# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:42:11 2017

@author: Kaustav
"""

import numpy
randn = numpy.random.randn
from pandas import *
s = Series(randn(3),('a','b','c'))
print(s)
print(s.mean())
print(s.index)
s=s.reindex(['c','b','a'])
print(s)
s+s
numpy.exp(s)

d = {'one':s*s,'two':s+s}
df = DataFrame(d)
print(df)
df.index
df.columns
df.values
df['three'] = s*3
df['one']
df.one
df.drop('c')
df.drop(['b','a'])
df.mean()
df.count()
df.sum()
df.median()
df.min()
df.max()
df.abs()
df.prod()
df.std()
df.var()
df.skew()
df.kurt()
df.quantile()
df.cumsum()
df.cummax()
df.cummin()

from pandas import *
s1=Series(randn(1000))
s2=Series(randn(1000))
print(s1.cov(s2))
print(s1.corr(s2))
print(s1.corr(s2,method='spearman'))

