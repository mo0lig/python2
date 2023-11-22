import matplotlib.pyplot as plt
import numpy as np
figure, axes = plt.subplots()
circle1 = plt.Circle( (0.5, 0.4 ),0.3 ,fill = False )
circle2 = plt.Circle( (0.5, 0.3 ),0.2 ,fill = False )
circle3 = plt.Circle( (0.5, 0.2 ),0.1 ,fill = False )
axes.set_aspect(1)
axes.add_artist(circle1)
axes.add_artist(circle2)
axes.add_artist(circle3)
plt.show()