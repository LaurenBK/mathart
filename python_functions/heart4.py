import numpy as np

def heart4(n = 1000000):
    t = np.arange(0, np.pi, np.pi/n)   
    x = -3.0/2*(np.sin(2*t))**3 + 3.0/10*(np.sin(2*t))**7 + 1.0/3*np.sin(400*t)*(np.sin(2*t))**2*(np.cos(6.0/5*t))**4
    y = np.sin(8.0/3*t + np.pi/6) + 1.0/4*(np.sin(8.0/3*t + np.pi/6))**3 + 1.0/3*np.cos(400*t)*np.sin(2*t)*(np.cos(6.0/5*t))**4
    data =  [x, y]
    data = np.array(data).T
    return(data)
