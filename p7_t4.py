import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
dots, = plt.plot([], [], '--', color='red', label='line')


def fractal(xi,yi,c1,c2,n):
    x,y=[], []
    x0,y0=xi,yi
    for k in range(int (n)  ) :
      xt=x0**2-y0**2+c1
      yt= 2*x0*y0+c2
      x.append(xt)
      y.append(yt)
      x0,y0=xt,yt
    return x,y

 
plt.axis('equal')
 
ax.set_xlim(0, 0.5)
ax.set_ylim(0.2, 0.7)


x0=0.1
y0=0.1
c1=0.3
c2=0.33


g,h = fractal(x0,y0,c1,c2,1000)
dots2, = plt.plot(g, h, 'o', color='blue', label='line')
 

def animate(i):
    dots.set_data(fractal(x0,y0,c1,c2,i))  


ani = animation.FuncAnimation(fig,
                        animate,
                        
                        frames=100,
                        interval=30)

                        
plt.show()
ani.save('my_anim.gif')
