## Section 4.9  APPLICATIONS TO MARKOV CHAINS

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

A = np.array([[-3, 1, 3], [2, -2, 3], [1, 1, -6]])
B = np.array([0, 0, 0])

x = np.linalg.solve(A, B)

print(x)
