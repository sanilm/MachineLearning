'''
Created on 11-Aug-2018

@author: sanil
'''

import numpy as np
import matplotlib.pyplot as plt
from plainbox.impl import color

x = np.random.uniform(low=20, high=100, size=(500,))

y = np.random.uniform(low=20, high=100, size=(500,))

plt.scatter(x, y,s=10)

plt.xlabel('x')
plt.ylabel('y')
plt.title('scatter plot')
plt.legend()
plt.show()




