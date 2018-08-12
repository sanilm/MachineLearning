'''
Created on 11-Aug-2018

@author: sanil
'''
import numpy as np
import matplotlib.pyplot as plt



slices=[7,2,2,13]
activities=['sleep','eat','work','play']
cols=['c','m','r','k']


plt.pie(slices,labels=activities,colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')

plt.title('pie chart')

plt.show()
