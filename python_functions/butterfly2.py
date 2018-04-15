import numpy as np

def butterfly2(n = 40000):
    k = np.arange(1,2)
    data = [[]] * len(k)   
    x = (6.0/5)*(np.cos(141*np.pi*k/40000))**9*(1-(1.0/2)*(np.sin(np.pi*k/40000))**3)*(1-(1.0/4)*(np.cos(2*np.pi*k/40000))**30*(1+(2.0/3)*(np.cos(30*np.pi*k/40000))**20))*(1-(1.0/3)*(np.sin(2*np.pi*k/40000))**30*(np.sin(6*np.pi*k/40000))**10*((1.0/2)+(1.0/2)*(np.sin(18*np.pi*k/40000))**10))
    y = np.cos(2*np.pi*k/40000)*(np.cos(141*np.pi*k/40000))**2*(1+(1.0/4)*(np.cos(np.pi*k/40000))**24*(np.cos(3*np.pi*k/40000))**24*(np.cos(19*np.pi*k/40000))**24)
    r = ((9.0/8)-(np.sin(2*np.pi*k/40000))**10)*((1.0/100)+(1.0/40)*((np.cos(141*np.pi*k/40000))**14+(np.sin(141*np.pi*k/40000))**6)*(1-(np.cos(np.pi*k/40000))**16*(np.cos(3*np.pi*k/40000))**16*(np.cos(12*np.pi*k/40000))**16))
    data =  [x, y, r]
    data = np.array(data).T
    return(data)
