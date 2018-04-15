import numpy as np

def heart3(n = 1000000):
    t = np.arange(0, np.pi, np.pi/n)   
    x = 1.0/6*np.sin(2*t)*(1 + np.cos(80*t))*(1 - 1.0/12*(np.sin(2*t))**8)
    y = -1.0/2*(2*t/np.pi - 1)**2 +  1.0/7*np.sin(2*t)*(np.sin(80*t))**8
    data =  [x, y]
    data = np.array(data).T
    return(data)
