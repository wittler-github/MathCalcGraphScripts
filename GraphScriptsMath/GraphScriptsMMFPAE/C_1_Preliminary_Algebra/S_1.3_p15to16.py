#### SECTION 1.3 page 15 to 16

##Auxiliary information from
#https://en.wikipedia.org/wiki/Conic_section
#Plot Conic sections from https://mmas.github.io/conics-matplotlib

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['lines.color'] = 'b'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])
mpl.rcParams["figure.edgecolor"] ='k'
mpl.rcParams["figure.figsize"] = [2*6.4, 1.4*6.4]


fig, SP = plt.subplots(2, 3)

fig.subplots_adjust(hspace = 0.5, wspace = 0.01)

SPcpa = np.array(SP)
for i, spcp in enumerate(SPcpa.reshape(-1)):
  spcp.xaxis.set_major_locator(plt.MultipleLocator(1))
  spcp.yaxis.set_major_locator(plt.MultipleLocator(1))
  spcp.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
  spcp.yaxis.set_minor_locator(plt.MultipleLocator(0.5))
  spcp.grid(color='k', linestyle='-', linewidth=0.5)
  spcp.axis('equal')
  spcp.set_aspect('equal', 'box')


x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)


AC, BC , CC, DC, EC, FC = -4, -6, 5, -4, 7, 10
#assert CC**2 - 4*AC*BC == 0

a = 1
b = 1
alpha = 2
beta = 2

levels = [0,1,2,4,7]
Mcolors=['k','m','b', 'g','darkorange']


## CONIC SECTIONS GENERAL AND GENERIC EXAMPLE FORMS

SP[0,0].contour(x, y,(AC*(x**2) + BC*(y**2) + CC*(x*y) + + DC*x + EC*y + FC), levels, colors = Mcolors)
SP[0,0].set_title('GENERAL FORM')

SP[0,1].contour(x, y,(x-alpha)**2/a**2 + (y-beta)**2/b**2, levels, colors=Mcolors)
SP[0,1].set_title('ELLIPSE')

SP[0,2].contour(x, y,(y-beta)**2 - 4*a*(x-alpha), levels, colors=Mcolors)
SP[0,2].set_title('PARABOLA X-SYMMETRIC')

SP[1,0].contour(x, y,(x-alpha)**2/a**2 - (y-beta)**2/b**2, levels, colors=Mcolors)
SP[1,0].set_title('HYPERBOLA')

SP[1,1].contour(x, y,(x-alpha)**2 + (y-beta)**2, levels, colors=Mcolors)
SP[1,1].set_title('CIRCLE')

SP[1,2].contour(x, y,(x-alpha)**2 - 4*a*(y-beta), levels, colors=Mcolors)
SP[1,2].set_title('PARABOLA Y-SYMMETRIC')


plt.show()
