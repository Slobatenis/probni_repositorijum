# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 18:43:06 2018

@author: Fazi
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def budworm(x,t,r,K):
    return r*x*(1-x/K)-x**2/(1+x**2)

t = np.linspace(0,60,2000)
K = np.linspace(3,20,100)
r=0.45
x0 = [0.5,30]
naslov=['x1','x2']
x1=np.zeros(100) 
x2=np.zeros(100)  


for i in range(100):
    sol=integrate.odeint(budworm,x0[0],t,args=(r,K[i]))
    x1[i]=sol[1990]

for i in range(100):
    sol=integrate.odeint(budworm,x0[1],t,args=(r,K[i]))
    x2[i]=sol[1990]

plt.figure(2,figsize=(8,6),dpi=60)
plt.xlabel('Broj stabala')
plt.ylabel('Populacija moljaca')
plt.plot(K,x1,label='x0=0.5')
plt.plot(K,x2,label='x0=30')
plt.legend()