import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import math


def center(x,y,c):
    for i in range(len(x)):
        x[i] = x[i] - c[0]
    for i in range(len(y)):
        y[i] = y[i] - c[1]
    # return x,y  <--------------------- here
    return x,y

def recenter(x,y,c):
    for i in range(len(x)):
        x[i] = x[i] + c[0]
    for i in range(len(y)):
        y[i] = y[i] + c[1]
    # return x,y  <--------------------- here
    return x,y

def rotation(x,y,angle):
    my_list = [[],[]]
    for i in range(len(x)):
        my_list[0].append(x[i]*math.cos(angle) + y[i]*math.sin(angle))
    for j in range(len(y)):
        #Big mistake here, replace i by j <--------------------- here
        my_list[1].append(x[j]*math.sin(angle)*(-1.) + y[j]*math.cos(angle))
    return my_list[0], my_list[1]



fig = plt.figure()
ax = plt.axes(xlim=(10, 110), ylim=(-40, 60))
ax.set_aspect('equal')
line, = ax.plot([],[], lw=2)

def init():
    line.set_data([],[])
    return line,

def animate(i):
    c1 = 62.5
    c2 = 10
    pt_rot = (c1, c2)
    x = [47.5, 47.5, 77.5, 77.5, 47.5, 62.5, c1, 57.5, 67.5]
    y = [15, 45, 45, 15, 15, 15, c2, 10, 10]

    x,y = center(x,y,pt_rot)  # <--------------------- here
    x,y = rotation(x,y,(i/180.)*np.pi) # <------------ here
    x,y = recenter(x, y, pt_rot) # <------------------ here

    line.set_data(x,y)
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=359, interval=20, blit=True)

plt.show()
