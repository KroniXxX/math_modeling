import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

t=np.arange(-1, 1, 0.01)




def diff_func(v, x):
  y, x = v
  dydx= 3*x - 2*y +(np.exp)
  dzdx = z/x - y * z**2
  return dydx, dzdx



x0 = 5
y0 = -7


v0 = y0, z0


sol = odeint (diff_func, v0, x)

plt.plot(sol[:, 0], sol[:, 1], 'g')
plt.legend()
plt.show()









