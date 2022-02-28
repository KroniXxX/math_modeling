import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(-1, 1, 0.01)




def diff_func(v, t):
  y, x ,z = v
  dxdt= 3*x - y +z
  dydt = x + y + z
  dzdt = 4*x - y + 4*z
  return dxdt, dydt, dzdt 



y0 = 1
x0 = -71
z0 = -3 

v0 = y0, x0, z0


sol = odeint (diff_func, v0, t)

plt.plot(t, sol[:, 0], 'g')
plt.plot(t, sol[:, 1], 'b')
plt.plot(t, sol[:, 1], 'r')
plt.legend()
plt.show()

