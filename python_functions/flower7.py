import numpy as np

def flower7(n = 9000):
    k = np.arange(1,7)
    data = [[]] * len(k)   
    x = np.cos(14*np.pi*k/9000)*(1-(3.0/4)*(np.sin(20*np.pi*k/9000))**4-(1.0/4)*(np.cos(60*np.pi*k/9000))**3)
    y = np.sin(14*np.pi*k/9000)*(1-(3.0/4)*(np.sin(20*np.pi*k/9000))**4-(1.0/4)*(np.cos(60*np.pi*k/9000))**3)
    r = (1.0/120)+(1.0/18)*(np.sin(60*np.pi*k/9000))**4+(1.0/18)*(np.sin(160*np.pi*k/9000))**4
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
