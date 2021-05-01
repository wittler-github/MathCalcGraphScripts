#### SECTION 1.3 COORDINATE GEOMETRY page 16 to 17


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['lines.color'] = 'b'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])
mpl.rcParams["figure.edgecolor"] ='k'
mpl.rcParams["figure.figsize"] = [2*6.4, 1.4*6.4]


fig, SP = plt.subplots(1, 3)

fig.subplots_adjust(hspace = 1.5, wspace = 0.5)

SPcpa = np.array(SP)
for i, spcp in enumerate(SPcpa.reshape(-1)):
  spcp.xaxis.set_major_locator(plt.MultipleLocator(1))
  spcp.yaxis.set_major_locator(plt.MultipleLocator(1))
  spcp.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
  spcp.yaxis.set_minor_locator(plt.MultipleLocator(0.5))
  spcp.grid(color='k', linestyle='-', linewidth=0.5)
  spcp.axis('equal')
  spcp.set_aspect('equal', 'box')

## PARAMETERS

x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)

AC, BC , CC, DC, EC, FC = 1, 1, 0, 1, 1, 1
#assert CC**2 - 4*AC*BC == 0

a = 4
b = 2
alpha = 0
beta = 0

levels = [0,1,2,4,7]
Mcolors=['k','m','b', 'g','darkorange']


## CONIC SECTIONS GENERAL FORM CIRCLE

SP[0].contour(x, y,(AC*(x**2) + BC*(y**2) + CC*(x*y) + DC*x + EC*y + FC), levels, colors = Mcolors)
SP[0].set_title('GENERAL FORM CIRCLE AC=BC, CC=0')


## PARABOLA X-SYMMETRIC FOCI AND DIRECTRIX

SP[1].contour(x, y,(y-beta)**2 - 4*a*(x-alpha), [0], colors = 'k', alpha=.9)
SP[1].set_title('PARABOLA X-SYMMETRIC')
# Focus.
SP[1].plot(a,0,color='b',markersize=4,marker='o')
# Directrix.
SP[1].axvline(-a,color='b',linewidth=1.5)

## ELLIPSE FOCI AND DIRECTRIX

SP[2].contour(x, y,((x-alpha)**2)/(a**2) + ((y-beta)**2)/(b**2), [1], colors='k', alpha=.9)
SP[2].set_title('ELLIPSE')
# Eccentricity.
e = np.sqrt(((a**2) - b**2)/(a**2))
print("Eccentricity",e)
print("Foci",a*e)
print("Directrice",a/e)
print("Foci-Directrice",(a*e)-(a/e))
# Foci.
SP[2].plot(a*e, 0, '.', -a*e, 0, '.',color='b')
# Directrices.
SP[2].axvline(a/e,color='b')
SP[2].axvline(-a/e,color='b')


plt.show()
