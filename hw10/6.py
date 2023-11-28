import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(0, 16, 1000)
x = np.sin(z)
y = np.cos(z)
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, 'grey')
z = 15 * np.random.random(150)
x = np.sin(z) + 0.1 * np.random.randn(150)
y = np.cos(z) + 0.1 * np.random.randn(150)
ax.scatter3D(x, y, z, c=z, cmap='Greens')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()