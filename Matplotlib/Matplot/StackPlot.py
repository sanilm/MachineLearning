'''
Created on 11-Aug-2018

@author: sanil
'''
import numpy as np
import matplotlib.pyplot as plt


days=np.arange(7)

sleep=np.random.uniform(low=1, high=6, size=(7,))
eat=np.random.uniform(low=1, high=3, size=(7,))
work=np.random.uniform(low=1, high=9, size=(7,))
play=np.random.uniform(low=1, high=2, size=(7,))

print(sleep)
print(eat)
print(work)
print(play)

plt.stackplot(days,sleep,eat,work,play,colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('stack plot')
plt.legend()
plt.show()
