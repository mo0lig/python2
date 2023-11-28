import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.random.normal(loc=-.9, scale=.6, size=(4000,))
y = np.random.normal(loc=.2, scale=.25, size=(4000,))
z = np.random.normal(loc=0.2, scale=1, size=(4000,))

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_xlim(-2, 1.8)
ax.set_ylim(-2, 1.8)
ax.set_zlim(-2, 4)

ax.plot(x, y, '+', markersize=.25, color='r', zdir='z', zs=1.)
ax.plot(x, z, '+', markersize=.25, color='y', zdir='y', zs=0.8)
ax.plot(y, z, '+', markersize=.25, color='b', zdir='x', zs=-2.)
plt.show()