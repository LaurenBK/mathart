import numpy as np

def millipede(n = 3000):
    t = np.arange(0, np.pi, np.pi/n)   
    x = np.cos(2*t)+(1.0/17)*(np.sin(906*t))**2+(1.0/6)*(np.cos(t)*np.cos(6*t)*np.cos(18*t))**14*(np.cos(81*t))**10
    y = (1.0/10)*(np.cos(3*t))**2+(1.0/18)*(2+(np.sin(2*t))**2)*(np.cos(151*t))**9
    r = (1.0/300)+(4.0/185)*(np.sin(151*t))**10*(3+2*(np.sin(2*t))**2)
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
