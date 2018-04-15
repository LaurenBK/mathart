import numpy as np

def branch(n = 3000):
    k = np.arange(1,3000)
    data = [[]] * len(k)   
    x = (2*k/3000)+(1.0/17)*np.sin(np.pi*k/100)+(1.0/9)*(np.sin(np.pi*k/200))**8
    y = (1.0/4)*(k/3000)**2+(1.0/4)*(np.sin(np.pi*k/200))**5+(1.0/112)*np.sin(np.pi*k/100)
    r = (1.0/170)+(1.0/24)*(np.sin(np.pi*k/100))**2*(1-(np.cos(np.pi*k/200))**4)
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
