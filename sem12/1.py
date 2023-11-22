import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots()
ax.set_xlim((-1,1)) # interval of x axis
ax.set_ylim((0,1)) # interval of y axis
ax.set_xlabel("x")
ax.set_ylabel("y")
x = np.linspace(-1,1,100) 
ax.plot(x,x**2,label=r'$f(x)=\ x^2$')
ax.legend(loc='best', fontsize=8)
plt.savefig('figure_with_legend.png')
plt.show()
