import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

x=np.arange(0.001, 20, 0.01)

def diff_func(fff, arg):
  y, p = fff
  x =arg
  dydx = p
  dpdx = -((x**2) - 4) * (y/(x**2)) - (p/x)
  return dydx , dpdx




sol = odeint (diff_func, (0.00000001, 0), x)

plt.plot(x, sol[:, 0], 'g')

plt.legend()
plt.show()





