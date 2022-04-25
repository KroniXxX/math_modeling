import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 2
t = np.linspace(0, years*seconds_in_year, frames)

def move_func(s, t):
    (x1, v_x1, y1, v_y1, r) = s

    dxdt1 = v_x1
    dv_xdt1 = - G * m * x1 / (x1**2 + y1**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = - G * m * y1 / (x1**2 + y1**2)**1.5
    r=np.sqrt(dxdt1**2+dydt1**2)
    qs=1367*(r/149 597 870 700)
    qw=m*c*
    dmdt1 = -(((3*m*p/4*np.phi)**2/3)*qs)/(qw)
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1, dmdt1,)
G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)
cl=60*10**3
p=900
a = np.pi / 3 +np.pi
v= 40000

x10 = 0.5* (10 **11)
v_x10 = v * np.sin(a) 
y10 =  200 * (10 **9)
v_y10 = v* np.cos(a)
r=np.sqrt(x10**2+y10**2)


s0 = (x10, v_x10, y10, v_y10, r)
