import matplotlib.pyplot as plt
names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
values = [25, 48, 73, 10, 20, 68, 30]
colors = ['red', 'green', 'yellow', 'pink', 'purple', 'blue', 'black']
plt.bar(names, values, color=colors, alpha=0.7)
plt.title('Data')
plt.show()