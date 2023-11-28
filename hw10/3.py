import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(0,15.*np.pi, 100)
f2 = np.linspace(np.pi,3.*np.pi, 100)
f3 = np.linspace(0,2*np.pi, 100)

plt.plot(y, np.sin(f2))
plt.plot(y, np.cos(f2))

plt.plot(y, np.sin(f3))
plt.plot(y, np.cos(f3))

plt.grid(True)
plt.xlim(0, 50)
plt.show()