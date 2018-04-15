import numpy as np

def leaves(n = 30000):
    k = np.arange(1,30000)
    data = [[]] * len(k)   
    x = (3.0/2)*(np.sin((2*np.pi*k/30000)+(np.pi/3)))**7
    y = (1.0/4)*(np.cos(6*np.pi*k/30000))**2*(2-(np.sin((2*np.pi*k/30000)+(np.pi/3)))**4-2*(np.cos(np.pi*k/30))**2)-(1.0/2)*(np.cos((2*np.pi*k/30000)+(np.pi/3)))**2
    r = (1.0/140)+(1.0/70)*(np.cos((2*np.pi*k/30000)+(np.pi/3)))**10
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
