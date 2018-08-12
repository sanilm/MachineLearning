'''
Created on 11-Aug-2018

@author: sanil
'''

import numpy as np
import matplotlib.pyplot as plt
from plainbox.impl import color

sampl = np.random.uniform(low=20, high=100, size=(20,))

bins=np.arange(20,100,10)

print(sampl)
print(bins)

plt.hist(sampl, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('bar graph')
plt.legend()
plt.show()




