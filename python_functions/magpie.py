import numpy as np

def magnp.pie(n = 200000):
  data.frame(k = seq(-10000, 10000, 20000/n)   
    x = (11*k/100000)+(np.cos(41*np.pi*k/10000))**6*np.sin((k/10000)**7*(np.pi/2))
    y = -(np.cos(41*np.pi*k/10000))**6*np.cos((k/10000)**7*(np.pi/2))*(1+(5.0/2)*(np.cos(3*np.pi*k/100000)*np.cos(9*np.pi*k/100000))**8)+(1.0/2)*(np.cos(np.pi*k/40000)*np.cos(3*np.pi*k/40000)*np.cos(3*np.pi*k/20000))**10
    r = (1.0/50)+(1.0/20)*(np.sin(41*np.pi*k/10000)*np.sin(np.pi*k/10000))**2
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
