
import matplotlib.pyplot as plt
V1=343
v=int(input('скрость тела:'))

if (v < V1):
  circle1 = plt.Circle((5 , 5), 1, color='y',fill=False)

  circle2 = plt.Circle((5 , 5), 2, color='y' ,fill=False)

  circle3 = plt.Circle((5 , 5), 3, color='y' ,fill=False)

  circle4 = plt.Circle((5 , 5), 4, color='y' ,fill=False)

  fig, ax = plt.subplots() 
  ax.set_xlim((0, 10))
  ax.set_ylim((0, 10))
  ax.add_artist(circle1)

  ax.add_artist(circle2)

  ax.add_artist(circle3)

  ax.add_artist(circle4)

  fig.savefig('plotcircles.png')


elif (v == V1):
  circle1 = plt.Circle((10 , 7), 1, color='y',fill=False)

  circle2 = plt.Circle((9 , 7), 2, color='y' ,fill=False)

  circle3 = plt.Circle((7 , 7), 4, color='y' ,fill=False)

  circle4 = plt.Circle((4 , 7), 8, color='y' ,fill=False)

  fig, ax = plt.subplots() 
  ax.set_xlim((0, 25))
  ax.set_ylim((0, 25))
  ax.add_artist(circle1)

  ax.add_artist(circle2)

  ax.add_artist(circle3)

  ax.add_artist(circle4)

  fig.savefig('plotcircles.png')



elif (v > V1):
  circle1 = plt.Circle((6 , 10), 1, color='y',fill=False)

  circle2 = plt.Circle((8 , 10), 2, color='y' ,fill=False)

  circle3 = plt.Circle((10 , 10), 3, color='y' ,fill=False)

  circle4 = plt.Circle((13 , 10), 4, color='y' ,fill=False)

  fig, ax = plt.subplots() 
  ax.set_xlim((0, 20))
  ax.set_ylim((0, 20))
  ax.add_artist(circle1)

  ax.add_artist(circle2)

  ax.add_artist(circle3)

  ax.add_artist(circle4)

  fig.savefig('plotcircles.png')
