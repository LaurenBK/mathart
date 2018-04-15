import numpy as np

def heart2(n = 1000000):
  A <- function(t):
    1 + 1/2*(cos(36*t))^10*(1 + 1/2*(cos(108*t))^12)
  }
    t = np.arange(0, np.pi, np.pi/n)   
    x = 2.0/3*np.cos(2*t)*(1 - 1.0/7*(np.cos(12*t))**4*A(t)) + 1.0/4*np.sin(22*t + np.pi/2)
    y = 2.0/3*np.sin(2*t)*(1 - 1.0/7*(np.cos(12*t))**4*A(t)) + 1.0/4*np.cos(22*t + np.pi/2)
    data =  [x, y]
    data = np.array(data).T
    return(data)
