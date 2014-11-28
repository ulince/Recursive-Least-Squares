
"""
Created on Mon Sep 01 16:22:35 2014
Minimos cuadrados recursivo
@author: Ulysses Lince Romero
144088
"""
import numpy as np
import pylab as pl

s=np.random.randn(12,1)
COEF=np.zeros([2,len(s)])
yest=np.zeros(len(s))
x=np.linspace(0,10,len(s)-1,endpoint=True)
t = 0

def getCoefs(t,c):
    if t == len(s) - 1:
        return c
    else:
        coef = np.dot(np.linalg.pinv(getMtx(t)),getInter(t))
        COEF[0:2,[t]] = coef
        return getCoefs(t+1,coef)
        
def getMtx(t):
    vect_old = s[[t-1,t]]
    vT_old = np.transpose(vect_old)
    Mtx_old = np.dot(vect_old,vT_old)
    vect_new = s[[t,t+1]]
    vT_new = np.transpose(vect_new)
    Mtx_new = np.dot(vect_new, vT_new)
    return Mtx_old + Mtx_new
        
def getInter(t):
    vect_old = s[[t-1,t]]
    y_old = [s[t-1],s[t-1]]        
    Inter_old = vect_old*y_old
    vect_new = s[[t,t+1]]
    y_new = [s[t],s[t]]        
    Inter_new = vect_new*y_new
    return Inter_old + Inter_new
    
def getYest():
    for t in range(10):
        vect=s[[t,t+1]]
        vT=np.transpose(vect)
        temp = [[COEF[0,t]],[COEF[1,t]]]
        yest[t] = np.dot(vT,temp)


a = getCoefs(t,[[0],[0]])  
getYest()  
pl.plot(x,s[0:len(s)-1],'bo')
pl.plot(x,yest[0:len(s)-1],'r-')
pl.show()

