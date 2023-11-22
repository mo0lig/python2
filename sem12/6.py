import matplotlib.pyplot as plt
import numpy as np
springx = np.random.uniform(0, 0.6, size=150)
springy = np.random.uniform(0, 8000, size=150)
summerx = np.random.uniform(0, 0.8, size=150)
summery = np.random.uniform(1000, 8000, size=150)
fallx = np.random.uniform(0.45, 0.85, size=150)
fally = np.random.uniform(1000, 9000, size=150)
winterx = np.random.uniform(0.2, 0.85, size=150)
wintery = np.random.uniform(1000, 9000, size=150)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].scatter(springx, springy, c='green', label='Spring', alpha=0.6)
axs[0, 0].set_title('Spring')
axs[0, 0].set_xlim(0, 0.6)
axs[0, 0].set_ylim(0, 9000)

axs[0, 1].scatter(summerx, summery, c='yellow', label='Summer', alpha=0.6)
axs[0, 1].set_title('Summer')
axs[0, 1].set_xlim(0, 0.8)
axs[0, 1].set_ylim(0, 9000)

axs[1, 0].scatter(fallx, fally, c='brown', label='Fall', alpha=0.6)
axs[1, 0].set_title('Fall')
axs[1, 0].set_xlim(0.45, 0.85)
axs[1, 0].set_ylim(1000, 9000)

axs[1, 1].scatter(winterx, wintery, c='blue', label='Winter', alpha=0.6)
axs[1, 1].set_title('Winter')
axs[1, 1].set_xlim(0.2,0.85)
axs[1, 1].set_ylim(0, 9000)

plt.tight_layout()

# Show the plot
plt.show()