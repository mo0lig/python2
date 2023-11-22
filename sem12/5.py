import numpy as np
import matplotlib.pyplot as plt
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
area = np.pi * (13 * np.random.rand(100))**2 

plt.scatter(x, y, s=area, c=colors, alpha=0.6)
plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)

plt.show()