import numpy as np

def harmonograph(n = 1000000,
                         A1 = 1, A2 = 1, A3 = 1, A4 = 1,
                         d1 = 0.039, d2 = 0.006, d3 = 0, d4 = 0.0045,
                         f1 = 10, f2 = 3, f3 = 1, f4 = 2,
                         p1 = 0, p2 = 0, p3 = np.pi/2, p4 = 0):
    t = np.arange(0, 200*np.pi, 200*np.pi/n)   
    x = A1*np.sin(t*f1+p1)*np.exp(-d1*t) + A2*np.sin(t*f2+p2)*np.exp(-d2*t)
    y = A3*np.sin(t*f3+p3)*np.exp(-d3*t) + A4*np.sin(t*f4+p4)*np.exp(-d4*t)
    data =  [x, y]
    data = np.array(data).T
    return(data)
