import matplotlib.pyplot as plt
import numpy as np

categories = ['Water', 'Tea', 'Coffee']
coffee_values = np.random.rand(100)
tea_values = np.random.rand(100)
water_values = np.random.rand(100)

x1 = np.random.uniform(0, 0.3, size=len(water_values))
y1 = np.random.uniform(0, 0.3, size=len(water_values))
x2 = np.random.uniform(0.4, 0.8, size=len(water_values))
y2 = np.random.uniform(0.0, 0.5, size=len(water_values))
x3 = np.random.uniform(0.7, 1.2, size=len(water_values))
y3 = np.random.uniform(0, 1.1, size=len(water_values))

plt.scatter(x1, y1,  c='blue', marker='.', s=100, alpha=0.7)
plt.scatter(x2, y2,  c='green', marker='.', s=100, alpha=0.7)
plt.scatter(x3, y3,  c='red', marker='.', s=100, alpha=0.7)

plt.title('matplot scatter plot')

plt.legend(categories)
plt.show()