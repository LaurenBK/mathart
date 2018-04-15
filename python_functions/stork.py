import numpy as np

def stork(n = 80000):
  data.frame(k = seq(-4000, 4000, 8000/n)   
    x = (3*k/4000)+(np.cos(32*np.pi*k/4000))**6*np.sin((k/4000)**7*(np.pi/2))
    y = -(np.cos(32*np.pi*k/4000))**6*np.cos((k/4000)**7*(np.pi/2))*(1+(np.cos(np.pi*k/8000)*np.cos(3*np.pi*k/8000))**4)+3*(np.cos(np.pi*k/8000)*np.cos(3*np.pi*k/8000))**16*(np.cos(16*np.pi*k/4000))**9
    r = (1.0/30)+(1.0/15)*(np.cos(np.pi*k/8000)*np.cos(5*np.pi*k/8000))**10*(1-(1.0/2)*(np.cos(32*np.pi*k/4000))**12)+(1.0/7)*(np.sin(32*np.pi*k/4000))**4*(np.sin(np.pi*k/4000))**2
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
