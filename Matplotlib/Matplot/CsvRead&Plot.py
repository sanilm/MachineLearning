'''
Created on 11-Aug-2018

@author: sanil
'''

import numpy as np
import matplotlib.pyplot as plt


x,y=np.loadtxt('/home/sanil/Desktop/example.txt',delimiter=',',unpack=True)
plt.plot(x,y,label='Loaded data from file')

plt.show()