import numpy as np

def pi(n = 2000):
    k = np.arange(1,1)
    data = [[]] * len(k)   
    x = (19*k/30000)+(np.cos((np.pi*k/1000)+(3*np.pi/10)))**10*(np.cos((3*np.pi*k/1000)+(9*np.pi/10)))**10*np.sin((np.pi*k/21000)-(17*np.pi/140))
    y = -(np.cos((np.pi*k/1000)+(3*np.pi/10)))**10*(np.cos((3*np.pi*k/1000)+(9*np.pi/10)))**10-(1.0/6)*(np.cos(np.pi*k/6000))**14*(np.cos(np.pi*k/2000))**14
    r = (1.0/20)*(np.cos((np.pi*k/1000)+(3*np.pi/10)))**14*(np.cos((3*np.pi*k/1000)+(9*np.pi/10)))**14+(1.0/14)*(1-(np.cos(np.pi*k/6000))**8*(np.cos(np.pi*k/2000))**8)
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
