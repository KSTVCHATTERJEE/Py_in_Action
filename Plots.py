# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:57:36 2017

@author: Kaustav
"""

import matplotlib.pyplot as plt
year=[1950,1970,1990,2010]
pop=[2.519,3.692,5.263,6.972]
plt.plot(year,pop)
plt.show()


import matplotlib.pyplot as plt
year=[1950,1970,1990,2010]
pop=[2.519,3.692,5.263,6.972]
plt.scatter(year,pop)
plt.show()

values=[0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values)
plt.show()

import matplotlib.pyplot as plt
year = [1950,1951,1952,2100]
pop = [2.538,2.57,2.62, 10.85]

#add more data
year = [1800,1850,1900] + year
pop = [1.0,1.262,1.650] + pop

plt.plot(year,pop)

plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population Projections")
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])

plt.show()

import numpy as np
import matplotlib.pyplot as plt

#evenly sampled time at .2 intervals
t = np.arange(0., 5., 0.2)

#red dashes, blue squares and green triangles
plt.scatter(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.axis([0,6,0,150]) #x and y range of axis
plt.show()

import numpy as np
import matplotlib.pyplot as plt
mu,sigma = 100,15
x=mu+sigma*np.random.randn(10000)
#the histogram of the data
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.hist(x,50,facecolor='g')
plt.text(60,.025,r'$\mu=100,\ \sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()










