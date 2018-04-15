import numpy as np

def palm_branch(n = 12000):
    k = np.arange(1,12000)
    data = [[]] * len(k)   
    x = (2*k/12000)+(1.0/7)*(np.sin(91*np.pi*k/12000))**8*(1-(np.cos(np.pi*k/24000)*np.cos(3*np.pi*k/24000))**10)+(1.0/4)*(np.sin(91*np.pi*k/12000))**6*np.sin((2*np.pi/5)*(k/12000)**12)
    y = (1.0/3)*np.sin(np.pi*k/24000)+(1.0/4)*(np.sin(91*np.pi*k/12000))**5*np.cos((np.pi/2)*(k/12000)**12)*(1-(np.cos(np.pi*k/24000)*np.cos(3*np.pi*k/24000))**10)
    r = (1.0/270)+(1.0/140)*(np.sin(182*np.pi*k/12000))**2*(1-(np.cos(91*np.pi*k/12000))**4)+(1.0/80)*(np.cos(91*np.pi*k/12000))**6
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
