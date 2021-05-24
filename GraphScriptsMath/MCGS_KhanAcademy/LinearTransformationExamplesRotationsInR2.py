import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from matplotlib.ticker import MaxNLocator
from matplotlib import rc
import matplotlib as mpl

fig = plt.figure(figsize=(8, 8))
ax = plt.gca()

ax.set_xlim([-10.0,10.0])
ax.set_ylim([-10.0,10.0])

ax.axis('equal')
ax.grid()
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.xaxis.grid(True,'major',linewidth=1.0, color='k')
ax.xaxis.grid(True,'minor',linewidth=0.5,color='gray')
ax.yaxis.grid(True,'major',linewidth=1.0, color='k')
ax.yaxis.grid(True,'minor',linewidth=0.5,color='gray')

theta = np.radians(45)
c, s = np.cos(theta), np.sin(theta)

A = np.array([[1.0,0.0],[2.0,0.0],[1.0,1.0],[2.0,1.0]])

colors=list('bgrcmykw')

ax.scatter(0,0, c='y', s=200)

for i, x in enumerate(A):
    print("iteration A index =",i)
    print("iteration A vector", x)
    ax.scatter(x[0],x[1],c=colors[i], s=200,alpha=0.25)
    ax.quiver(0,0,x[0],x[1],color=colors[i],scale=1,scale_units='xy',alpha=0.25)

R = np.array(((c, -s), (s, c)))

RA = np.dot(R,A.T)

for i, x in enumerate(RA.T):
    print("iteration RA index=",i)
    print("iteration RA vector", x)
    ax.scatter(x[0],x[1], c=colors[i], s=200)
    ax.quiver(0,0,x[0],x[1], color=colors[i],scale=1,scale_units='xy',alpha=1.0)

print("Matrix A =", A)
print("Dimensions of A =", A.shape)
print("Matrix A.T =", A.T)
print("Dimensions of A.T =", A.T.shape)
print("Matrix RA =", RA)
print("Dimensions of RA =", RA.shape)
print("Matrix RA.T =", RA.T)
print("Dimensions of RA.T =", RA.T.shape)

plt.xlim(-4,4)
plt.ylim(-4,4)

plt.show()
