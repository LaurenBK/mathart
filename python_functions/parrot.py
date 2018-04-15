import numpy as np

def parrot(n = 200000):
  data.frame(k = seq(-10000, 10000, 20000/n)   
    x = (3*k/20000)+(np.cos(37*np.pi*k/10000))**6*np.sin((k/10000)**7*(3*np.pi/5))+(9.0/7)*(np.cos(37*np.pi*k/10000))**16*(np.cos(np.pi*k/20000))**12*np.sin(np.pi*k/10000)
    y = (-5.0/4)*(np.cos(37*np.pi*k/10000))**6*np.cos((k/10000)**7*(3*np.pi/5))*(1+3*(np.cos(np.pi*k/20000)*np.cos(3*np.pi*k/20000))**8)+(2.0/3)*(np.cos(3*np.pi*k/200000)*np.cos(9*np.pi*k/200000)*np.cos(9*np.pi*k/100000))**12
    r = (1.0/32)+(1.0/15)*(np.sin(37*np.pi*k/10000))**2*((np.sin(np.pi*k/10000))**2+(3.0/2)*(np.cos(np.pi*k/20000))**18)
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
