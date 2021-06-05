import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from matplotlib.ticker import MaxNLocator
from matplotlib import rc
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


import numpy as np
import math as m

def Rx(angle):
  return np.matrix([[ 1, 0           , 0           ],
                   [ 0, m.cos(angle),-m.sin(angle)],
                   [ 0, m.sin(angle), m.cos(angle)]])

## Ry, Rz Not defined in KA video
def Ry(angle):
  return np.matrix([[ m.cos(angle), 0, m.sin(angle)],
                   [ 0           , 1, 0           ],
                   [-m.sin(angle), 0, m.cos(angle)]])

def Rz(angle):
  return np.matrix([[ m.cos(angle), -m.sin(angle), 0 ],
                   [ m.sin(angle), m.cos(angle) , 0 ],
                   [ 0           , 0            , 1 ]])


angle_x = 0#m.pi/2
angle_y = m.pi/2
angle_z = 0#m.pi/2
print("angle_x =", angle_x)
print("angle_y  =", angle_y)
print("angle_z =", angle_z)


R = Rx(angle_x) * Ry(angle_y) * Rz(angle_z)
print(np.round(R, decimals=2))

v1 = np.array([[1],[0],[0]])
v2 = R * v1
print(np.round(v2, decimals=2))

colors=list('bgrcmykw')

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111, projection='3d')

#ax.scatter(v1[0],v1[1],v1[2],c=colors[2], s=200,alpha=0.25)
ax.quiver3D(0,0,0,v1[0],v1[1],v1[2],color='g',linewidth=3.3,alpha=1,label='Initial Vector')
ax.quiver3D(0,0,0,v2[0],v2[1],v2[2],color='m',linewidth=10,alpha=0.25,label='Rotated Vector')

ax.legend()

ax.set_xlabel('X',color=colors[0],fontsize=20)
ax.set_ylabel('Y',color=colors[3],fontsize=20)
ax.set_zlabel('Z',color=colors[4],fontsize=20)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)
#ax.axis('equal')
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1))
ax.zaxis.set_major_locator(plt.MultipleLocator(1))
ax.grid(True)


#plt.title('Initial and Rotated Vectors')

plt.draw()
plt.show()
