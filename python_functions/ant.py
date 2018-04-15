import numpy as np

def ant(n = 3000):
    t = np.arange(0, np.pi, np.pi/n)   
    x = (np.cos(7*t))**9*(np.cos(21*t))**10*(np.cos(70*t))**8
    y = np.cos(2*t)+(np.cos(80*t))**2*(np.cos(10*t)*np.cos(t))**10+(1.0/3)*(np.sin(420*t))**4-(2.0/3)*(np.sin(t)*np.sin(5*t))**10
    r = (1.0/150)+(1.0/30)*(np.sin(840*t))**2+(1.0/3)*(np.sin(7*t))**8
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
