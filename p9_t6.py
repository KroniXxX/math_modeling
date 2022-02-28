import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x=np.arange(0.01, 5, 0.01)


def diff_func(fff,  arg):
  x = arg
  s, y = fff
  dydx = s
  dsdx = s**2/y - 3*y/np.sqrt(x) 
  return dydx, dsdx


sol = odeint (diff_func, (0, 1), x)

plt.plot(x, sol[:, 0], 'g')
plt.plot(x, sol[:, 1], 'b')

plt.legend()
plt.show()

