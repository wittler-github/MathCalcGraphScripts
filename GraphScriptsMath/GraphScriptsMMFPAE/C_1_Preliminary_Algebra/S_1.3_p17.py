## Section 1.3 page 17 - parametric representations of conic sections

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['lines.color'] = 'b'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['b'])
mpl.rcParams["figure.edgecolor"] ='k'
mpl.rcParams['legend.fontsize'] = 12
mpl.rcParams["figure.figsize"] = [2*6.4, 1.4*6.4]

fig, SP = plt.subplots(1, 3)

fig.subplots_adjust(hspace = 1.5, wspace = 0.5)

SP[0].xaxis.set_major_locator(plt.MultipleLocator(1))
SP[0].yaxis.set_major_locator(plt.MultipleLocator(1))
SP[0].xaxis.set_minor_locator(plt.MultipleLocator(0.5))
SP[0].yaxis.set_minor_locator(plt.MultipleLocator(0.5))
SP[0].grid(color='k', linestyle='-', linewidth=0.5)
SP[0].axis('equal')
SP[0].set_aspect('equal', 'box')

SP[1].xaxis.set_major_locator(plt.MultipleLocator(100))
SP[1].yaxis.set_major_locator(plt.MultipleLocator(10))
SP[1].xaxis.set_minor_locator(plt.MultipleLocator(10))
SP[1].yaxis.set_minor_locator(plt.MultipleLocator(1))
SP[1].grid(color='k', linestyle='-', linewidth=0.5)
#SP[1].axis('equal')
#SP[1].set_aspect('equal', 'box')

# SP[2].xaxis.set_major_locator(plt.MultipleLocator(1000))
# SP[2].yaxis.set_major_locator(plt.MultipleLocator(1000))
# SP[2].xaxis.set_minor_locator(plt.MultipleLocator(50))
# SP[2].yaxis.set_minor_locator(plt.MultipleLocator(50))
SP[2].xaxis.set_tick_params(rotation=45)
SP[2].grid(color='k', linestyle='-', linewidth=0.5)
SP[2].axis('equal')
SP[2].set_aspect('equal', 'box')

phi = np.linspace(-4*np.pi, 4*np.pi, 50)
t = np.linspace(-4*np.pi, 4*np.pi, 50)

a = 1
b = 1
alpha = -500
beta = -500

xe = alpha + a*np.cos(phi)
ye = beta + b*np.sin(phi)
SP[0].scatter(xe, ye, label='ELLIPSE',color='b')
SP[0].legend()

xp = alpha + a*pow(t,2)
yp = beta + 2*a*t
SP[1].scatter(xp, yp, label='PARABOLA',color='g')
SP[1].legend()

xh = alpha + a*np.cosh(phi)
yh = beta + b*np.sinh(phi)
SP[2].scatter(xh, yh, label='HYPERBOLA',color='m')
SP[2].legend()

plt.show()
