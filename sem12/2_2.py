import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 51)
y = np.linspace(0, 8, 41)
(X, Y) = np.meshgrid(x, y)
a = np.exp(-((X - 2.5) ** 2 + (Y - 4) ** 2) / 4) - np.exp(-((X - 7.5) ** 2 + (Y - 4) ** 2) / 4)

fig, ax = plt.subplots()
c = ax.contour(x, y, a)
l = ax.clabel(c)

ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()
