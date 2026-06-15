import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2* np.pi, 2 * np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)

plt.subplot(2,2,1)
plt.scatter(x, y)
plt.subplot(2,2,2)
plt.plot(x, y2, color="red")
plt.show()