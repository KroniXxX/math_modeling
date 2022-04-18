import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 2
t = np.linspace(0, years*seconds_in_year, frames)

def move_func(s, t):
    (x1, v_x1, y1, v_y1) = s

    dxdt1 = v_x1
    dv_xdt1 = - G * m * x1 / (x1**2 + y1**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = - G * m * y1 / (x1**2 + y1**2)**1.5
  
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1)
G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

a = np.pi / 3 +np.pi
v= 40000

x10 = 0.5* (10 **11)
v_x10 = v * np.sin(a) 
y10 =  200 * (10 **9)
v_y10 = v* np.cos(a)



s0 = (x10, v_x10, y10, v_y10)
sol = odeint(move_func, s0, t)
def solve_func(i, key):
    
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        
        
    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
        
    return ((x1, y1), )

fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color='b')


plt.plot([0], [0], 'o', color='y', ms=20)

def animate(i):
  ball1.set_data(solve_func(i, 'point')[0])
  ball_line1.set_data(solve_func(i, 'line')[0])

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 1.5 *  y10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('123.gif')



##мы берем энергии не для вакума











































