import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
line, = plt.plot([], [], '--', color='red', label='line')
 
edge = 30

 
plt.axis('equal')
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
x, y = [], []

def star():

  t = np.arange(-10,10,0.01)
  x = 12*np.cos(t) + 8*np.cos(1.5*t)
  y = 12*np.sin(t) - 8*np.sin(1.5*t)
  star, = plt.plot(x,y,'--', color='blue', label='line')
  t = np.pi /2
  X=x*np.cos(t) - y*np.sin(t)
  Y=y*np.cos(t) + x*np.sin(t)
  star, = plt.plot(X,Y,'--', color='red', label='line')  
star()
plt.show()

def rotate(x,y,v):
  X=x*np.cos(v) - y*np.sin(v)
  Y=y*np.cos(v) + x*np.sin(v)
  return X,Y
def animate(a):
  line.set_data(fractal(x,y,a)) 

animate()
ani = animation.FuncAnimation(fig,
                        animate,
                        
                        frames=100,
                        interval=30)

ani.save('my_anim.gif')
