import numpy as np
import matplotlib.pyplot as plt
# постоянная скорость звука
V1=343
v=int(input('скрость тела:'))
# Условвие при котором скорость тела меньше чем скорость звука
if (v < V1):
  circle1 = plt.Circle((5 , 5), 1, color='y',fill=False)
  
  circle2 = plt.Circle((4.5 , 5), 2, color='y' ,fill=False)

  circle3 = plt.Circle((4 , 5), 3, color='y' ,fill=False)

  circle4 = plt.Circle((3.5 , 5), 4, color='y' ,fill=False)
  
  fig, ax = plt.subplots() 
  ax.set_xlim((-2, 10))
  ax.set_ylim((0, 10))
  ax.add_artist(circle1)

  ax.add_artist(circle2)

  ax.add_artist(circle3)

  ax.add_artist(circle4)

  x= [5, 4.5, 4, 3.5]
  y = [5,5 ,5,5 ]
  plt.plot(x, y, color='r', marker='>', ms=5)
  
  fig.savefig('plotcircles.png')


elif (v == V1):
  circle1 = plt.Circle((17.5 , 12.5), 1, color='y',fill=False)

  circle2 = plt.Circle((16.5 , 12.5), 2, color='y' ,fill=False)

  circle3 = plt.Circle((14.5 , 12.5), 4, color='y' ,fill=False)

  circle4 = plt.Circle((10.5 , 12.5), 8, color='y' ,fill=False)

  fig, ax = plt.subplots() 
  ax.set_xlim((0, 25))
  ax.set_ylim((0, 25))
  ax.add_artist(circle1)

  ax.add_artist(circle2)

  ax.add_artist(circle3)

  ax.add_artist(circle4)
  x= [17.5, 16.5, 14.5, 10.5]
  y = [12.5, 12.5 ,12.5 ,12.5 ]
  plt.plot(x, y, color='r', marker='>', ms=5)

  fig.savefig('plotcircles.png')


elif (v > V1):
  circle1 = plt.Circle((14 , 10), 1, color='y',fill=False)

  circle2 = plt.Circle((12 , 10), 2, color='y' ,fill=False)

  circle3 = plt.Circle((10 , 10), 3, color='y' ,fill=False)

  circle4 = plt.Circle((7 , 10), 4, color='y' ,fill=False)

  fig, ax = plt.subplots() 
  ax.set_xlim((0, 20))
  ax.set_ylim((0, 20))
  ax.add_artist(circle1)

  ax.add_artist(circle2)

  ax.add_artist(circle3)

  ax.add_artist(circle4)
  x= [14, 12, 10, 7, 16 ,0] 

  y = [10, 10 ,10 ,10, 10, 19] 

  plt.plot(x, y, color='r', marker='>', ms=5)
  

  fig.savefig('plotcircles.png')
  i = v / V1
  f = i *180 /  np.pi  
  print(f)


