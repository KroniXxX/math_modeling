import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation


frames = 200
t = np.linspace(0, 10, frames)

g = 9.8
m = 10
alpha = 55
alpha_rad = np.radians(alpha)
v0 = 2000

x0 = 0
v_x0 = v0 * np.cos(alpha_rad)
y0 = 0
v_y0 = v0 * np.sin(alpha_rad)

ff0 = x0, v_x0, y0, v_y0

k = [0, 0.7, 50]
index = 1


def diff_func(ff, t):
    x, v_x, y, v_y = ff
    v = np.sqrt(v_x ** 2 + v_y ** 2)
    dxdt = v_x
    dv_xdt = 0 - k[index]*(v ** 2)*(v_x/v)
    dydt = v_y
    dv_ydt = - g - k[index]*(v ** 2)*(v_y/v)
    return dxdt, dv_xdt, dydt, dv_ydt


def solve_func(i, key, solution):
    if key == 'p':
        x = solution[i, 0]
        y = solution[i, 2]
    else:
        x = solution[:i, 0]
        y = solution[:i, 2]
    return x, y


if __name__ == '__main__':
    sol = odeint(diff_func, ff0, t)
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r')
    ball_line, = plt.plot([], [], '-', color='r')

    def animate(i):
        ball.set_data(solve_func(i, 'p', sol))
        ball_line.set_data(solve_func(i, 'l', sol))

    ani = FuncAnimation(fig, animate, frames=frames, interval=30)

    edge = 15
    ax.set_xlim(0, edge*2)
    ax.set_ylim(0, edge)

    plt.show()
    ani.save('my_anim.gif')