# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:32:49 2020

@author: benho
"""

#%%
# Acknowledgement:
# https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-introduction
#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
n = 400
susceptible = np.zeros(n)
infected = np.zeros(n)
recovered = np.zeros(n)
time = np.zeros(n)

delta_t = .25
#%%
susceptible[0] = 1 # this is just 1, not 1 million b/c represents fraction
infected[0] = .000015
recovered[0] = 0
time[0] = 0 #time is measured in days

#%%
b = .9 # number of infected encounters per day
k = .07 # fraction that recovers each day
# these values are estimates
#%%
for i in range(n-1):
    ds = -b*susceptible[i]*infected[i]
    di = b*susceptible[i]*infected[i]-k*infected[i]
    dr = k*infected[i]
    
    susceptible[i+1] = susceptible[i] + ds*delta_t
    infected[i+1] = infected[i] + di*delta_t
    recovered[i+1] = recovered[i] + dr*delta_t
    
    time[i+1] = time[i] + delta_t

#%%
plt.figure()
plt.xlabel("time in days")
plt.grid()
plt.plot(time,susceptible)
plt.plot(time,infected)
plt.plot(time,recovered)
plt.legend(labels=["Susceptible","Infected","Recovered"])
plt.text(5,0.8,r'b={} k={}'.format(b,k))
plt.show()
