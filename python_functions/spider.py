import numpy as np

def snp.pider(n = 3000):
    t = np.arange(0, np.pi, np.pi/n)   
    x = (np.cos(7*t))**9*(np.cos(21*t))**10*(np.cos(70*t))**8*(1+(1.0/3)*(np.sin(5*t))**2)
    y = (1.0/4)*np.cos(2*t)+(np.cos(210*t))**3*(np.cos(7*t)*np.cos(21*t))**10*np.cos((8.0/5)*t+(np.pi/5))-(1.0/2)*(np.sin(t)*np.sin(5*t))**10
    r = (1.0/32)+(1.0/6)*(np.sin(7*t))**4+(1.0/6)*(np.sin(t))**8*(np.sin(5*t)*np.sin(15*t))**10-(1.0/40)*(np.cos(1260*t))**6
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
