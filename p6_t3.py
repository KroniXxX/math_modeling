import matplotlib.pyplot as plt
import decimal
import numpy as np

xmin = -20
xmax = 20
dx = 0.1

xlist = np.around(np.arange(xmin, xmax, dx), decimals=4)

ylist = 1 / xlist

plt.plot(xlist, ylist)
plt.show()