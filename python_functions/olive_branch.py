import numpy as np

def olive_branch(n = 4000):
    k = np.arange(1,4000)
    data = [[]] * len(k)   
    x = (2*k/4000)+(1.0/28)*np.sin(42*np.pi*k/4000)+(1.0/9)*(np.sin(21*np.pi*k/4000))**8+(1.0/4)*(np.sin(21*np.pi*k/4000))**6*np.sin((2*np.pi/5)*(k/4000)**12)
    y = (1.0/4)*(k/4000)**2+(1.0/4)*((np.sin(21*np.pi*k/4000))**5+(1.0/28)*np.sin(42*np.pi*k/4000))*np.cos((np.pi/2)*(k/4000)**12)
    r = (1.0/170)+(1.0/67)*(np.sin(42*np.pi*k/4000))**2*(1-(np.cos(21*np.pi*k/4000))**4)
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
