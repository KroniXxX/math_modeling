import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

R=7
N=16
V=5
x0=2
y0=2

def tochka(R,N,V,x0,y0):
  coords_x=[]; coords_y=[]; varr_x = []; varr_y = []
  for i in range(N):
    
    alp= (np.pi *2*i)/N
    x,y = R*np.cos(alp) + x0, R*np.sin(alp) + y0
    vx,vy = V* np.cos(alp + (np.pi/2)) + x,  V* np.sin(alp + (np.pi/2)) + y
    coords_x.append(x)
    coords_y.append(y)
    varr_x.append(vx)
    varr_y.append(vy)
  return coords_x, coords_y, varr_x, varr_y


m = tochka(R,N,V,x0,y0)

plt.axis('equal')
plt.scatter(m[0], m[1]) 

plt.scatter(m[2], m[3]) 

for i in range(N):
  plt.arrow(m[0][i], m[1][i],m[2][i]-m[0][i], m[3][i]- m[1][i]) 
plt.show()







