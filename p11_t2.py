import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 20, frames)

def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4,
     x5, v_x5, y5, v_y5,
     x6, v_x6, y6, v_y6) = s

    dxdt1 = v_x1
    dv_xdt1 = k * x1 * q1 * Q / (((x1**2 + y1**2)**1.5) * m)
    dydt1 = v_y1
    dv_ydt1 = k * x1 * q1 * Q / (((x1**2 + y1**2)**1.5) * m)

    dxdt2 = v_x2
    dv_xdt2 = k * x2 * q2 * Q / (((x2**2 + y2**2)**1.5) * m)
    dydt2 = v_y2
    dv_ydt2 = k * x2 * q2 * Q / (((x2**2 + y2**2)**1.5) * m)

    dxdt3 = v_x3
    dv_xdt3 = k * x3 * q3  * Q / (((x3**2 + y3**2)**1.5) * m)
    dydt3 = v_y3
    dv_ydt3 = k * x3 * q3 * Q / (((x3**2 + y3**2)**1.5) * m)

    dxdt4 = v_x4
    dv_xdt4 = k * x4 * q4 * Q / (((x4**2 + y4**2)**1.5) * m)
    dydt4 = v_y4
    dv_ydt4 = k * x4 * q4 * Q / (((x4**2 + y4**2)**1.5) * m)
  
    dxdt5 = v_x5
    dv_xdt5 = k * x5 * q5 * Q / (((x5**2 + y5**2)**1.5) * m)
    dydt5 = v_y5
    dv_ydt5 = k * x5 * q5 * Q / (((x5**2 + y5**2)**1.5) * m)

    dxdt6 = v_x6
    dv_xdt6 =  k  * x6 * q6 * Q / (((x6**2 + y6**2)**1.5) * m)
    dydt6 = v_y6
    dv_ydt6 =  k  * x6  * q6 * Q/ (((x6**2 + y6**2)**1.5) * m)

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4,
            dxdt5, dv_xdt5, dydt5, dv_ydt5,
            dxdt6, dv_xdt6, dydt6, dv_ydt6)
k = - 9 * 10**9
m = 0.5
x10 =3
v_x10 = -1
y10 = 2
v_y10 = 0


x20 =3
v_x20 = -1
y20 = 1.5
v_y20 =0

x30=3
v_x30=-1
y30=1
v_y30=0

x40=3
v_x40 = -1
y40 = -1
v_y40 =0

x50=3
v_x50=-1
y50=-1.5
v_y50=0

x60=3
v_x60=-1
y60=-2
v_y60=0
q1= 3 * 10**(-9)

q2= 3 * 10**(-9)

q3= 3 * 10**(-9)

q4= 3 * 10**(-9)

q5= 3 * 10**(-9)

q6= 3 * 10**(-9)

Q= 30000000 * 10**(-9)

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60)
sol = odeint(move_func, s0, t)
def solve_func(i, key):
    
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        x2 = sol[i, 4]
        y2 = sol[i, 6]
        x3 = sol[i, 8]
        y3 = sol[i, 10]
        x4 = sol[i, 12]
        y4 = sol[i, 14]
        x5 = sol[i, 16]
        y5 = sol[i, 18]
        x6 = sol[i, 20]
        y6 = sol[i, 22]
        
    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
        x2 = sol[:i, 4]
        y2 = sol[:i, 6]
        x3 = sol[:i, 8]
        y3 = sol[:i, 10]
        x4 = sol[:i, 12]
        y4 = sol[:i, 14]
        x5 = sol[:i, 16]
        y5 = sol[:i, 18]
        x6 = sol[:i, 20]
        y6 = sol[:i, 22]
    return ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6))

fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color='b')

ball2, = plt.plot([], [], 'o', color='r')
ball_line2, = plt.plot([], [], '-', color='r')

ball3, = plt.plot([], [], 'o', color='g')
ball_line3, = plt.plot([], [], '-', color='g')

ball4, = plt.plot([], [], 'o', color='y')
ball_line4, = plt.plot([], [], '-', color='y')

ball5, = plt.plot([], [], 'o', color='b')
ball_line5, = plt.plot([], [], '-', color='b')

ball6, = plt.plot([], [], 'o', color='r')
ball_line6, = plt.plot([], [], '-', color='r')



plt.plot([0], [0], 'o', color='y', ms=20)

def animate(i):
    ball1.set_data(solve_func(i, 'point')[0])
    ball_line1.set_data(solve_func(i, 'line')[0])

    ball2.set_data(solve_func(i, 'point')[1])
    ball_line2.set_data(solve_func(i, 'line')[1])

    ball3.set_data(solve_func(i, 'point')[2])
    ball_line3.set_data(solve_func(i, 'line')[2])
    
    ball4.set_data(solve_func(i, 'point')[3])
    ball_line4.set_data(solve_func(i, 'line')[3])

    ball5.set_data(solve_func(i, 'point')[4])
    ball_line5.set_data(solve_func(i, 'line')[4])
  
    ball6.set_data(solve_func(i, 'point')[5])
    ball_line6.set_data(solve_func(i, 'line')[5])

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 7
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('my_anim.gif')