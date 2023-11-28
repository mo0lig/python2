from matplotlib import pyplot as plt
import numpy as np

dt = np.array([
          [0.04, 0.1],
          [0.13, 0.13],
          [0.2, 0.16],
          [0.23, 0.22],
          [0.25, 0.24],
          [0.28, 0.33],
          [0.32, 0.33],
          [0.33, 0.4],
          [0.34, 0.5],
          [0.42, 0.30],
          [0.09, 0.07],
          [0.05, 0.05],
          [0.16, 0.18],
          [0.36, 0.3],
          [0.45, 0.44],
          [0.43, 0.42],
          [0.49, 0.48],
          [0.50, 0.56],
          [0.53, 0.59],
          [0.57, 0.51],
          [0.58, 0.60]
])

x = dt[:, 0].reshape(dt.shape[0], 1)
X = np.append(x, np.ones((dt.shape[0], 1)), axis=1)
y = dt[:, 1].reshape(dt.shape[0], 1)

t = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
print(f'{t}')
y_line = X.dot(t)
plt.scatter(x, y)
plt.plot(x, y_line, 'r')
plt.title('Best fit line using regression method')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()