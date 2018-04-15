import numpy as np

def heart1(n = 1000000):
    t = np.arange(0, np.pi, np.pi/n)   
    x = 4.0/9*np.sin(2*t) + 1.0/2*(np.sin(t))**8*np.cos(3*t) + 1.0/8*np.sin(2*t)*(np.cos(247*t))**4
    y =     np.sin(t)   + 1.0/3*(np.sin(t))**8*np.sin(3*t) + 1.0/8*np.sin(2*t)*(np.sin(247*t))**4
    data =  [x, y]
    data = np.array(data).T
    return(data)
