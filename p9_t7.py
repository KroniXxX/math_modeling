import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

t=np.arange(0.001, 3, 0.01)

def diff_func(fff, arg):
  j, y = fff
  t =arg
  dydt = j
  djdt = np.sqrt(1 - j**2)
  return dydt , dpdt




sol = odeint (diff_func, (1, 0), t)

plt.plot(t, sol[:, 0], 'g')
plt.plot(t, sol[:, 1], 'r')
plt.legend()
plt.show()





