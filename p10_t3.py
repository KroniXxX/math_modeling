import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
frames = 200
t = np.linspace(0, 50, frames)
 
# Запись диф. уравнения в виде функции
def radio_function(ff, t):
    ma, mb, mc = ff
    
    dadt = - k1 * ma
    dbdt = - k2 * mb + (k1 * ma)
    dcdt = - k3 * mc + (k2 * mb)
    return dadt, dbdt, dcdt
 
ma0 = 1000
mb0 = 0
mc0 = 0
k1 = 0.3
k2 = 0.2
k3 = 0.1
ff0= ma0, mb0, mc0

sol = odeint(radio_function, ff0 ,t)


plt.plot(t, sol[:,0], 'b')

plt.plot(t, sol[:,1], 'r')

plt.plot(t, sol[:,2], 'g')

plt.legend()
plt.show()

