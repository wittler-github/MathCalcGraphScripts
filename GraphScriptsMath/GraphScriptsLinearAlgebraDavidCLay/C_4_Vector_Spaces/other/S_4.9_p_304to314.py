## Section 4.9  APPLICATIONS TO MARKOV CHAINS

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

print("\n EXAMPLE 1\n")

M = np.array([[ 0.9500, 0.0300], [ 0.0500, 0.9700]])
xk = np.array([0.600, 0.400])
xkpo = xk
x_nr = 0
print("Matrix M\n")

for i in range(2):
   for j in range(2):
      print(M[i][j], end = " ")
   print("\n")

print("Matrix M vector product iteration\n")

for x in range(0,16):
    print("\n x%s = %s" % (x_nr, np.around(xkpo,5)))
    xkpo = M.dot(xk)
    x_nr += 1
    xk = xkpo

print("\n END EXAMPLE 1\n")

print("\n EXAMPLE 2\n")

P = np.array([[ 0.7, 0.1 ,0.3], [ 0.2, 0.8 ,0.3], [ 0.1, 0.1 ,0.4]])
xk = np.array([1.0, 0.0, 0.0])
xkpo = xk
x_nr = 0
print("Matrix P\n")

for i in range(3):
   for j in range(3):
      print(P[i][j], end = " ")
   print("\n")

print("Matrix P vector product iteration\n")

for x in range(0,16):
    print("\n x%s = %s" % (x_nr, np.around(xkpo,5)))
    xkpo = P.dot(xk)
    x_nr += 1
    xk = xkpo

print("\n END EXAMPLE 2\n")

print("\n EXAMPLE 3\n")

P = np.array([[ 0.5, 0.2 ,0.3], [ 0.3, 0.8 ,0.3], [ 0.2, 0.0 ,0.4]])
xk = np.array([1.0, 0.0, 0.0])
xkpo = xk
x_nr = 0
print("Matrix P\n")

for i in range(3):
   for j in range(3):
      print(P[i][j], end = " ")
   print("\n")

print("Matrix P vector product iteration\n")

for x in range(0,16):
    print("\n x%s = %s" % (x_nr, np.around(xkpo,5)))
    xkpo = P.dot(xk)
    x_nr += 1
    xk = xkpo

print("\n END EXAMPLE 3\n")

print("\n EXAMPLE 4\n")

P = np.array([[ 0.5, 0.2 ,0.3], [ 0.3, 0.8 ,0.3], [ 0.2, 0.0 ,0.4]])
xk = np.array([0.3, 0.6, 0.1])
xkpo = xk
x_nr = 0
print("Matrix P\n")

for i in range(3):
   for j in range(3):
      print(P[i][j], end = " ")
   print("\n")

print("Matrix P vector product iteration\n")

for x in range(0,16):
    print("\n x%s = %s" % (x_nr, np.around(xkpo,5)))
    xkpo = P.dot(xk)
    x_nr += 1
    xk = xkpo

print("\n END EXAMPLE 4\n")
