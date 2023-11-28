import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(0, 2 * np.pi, 150)
x = 16 * (np.sin(t)**3)
y = 13 * np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
plt.plot(x, y)
plt.fill(x,y)
plt.title('Heart')
plt.show()