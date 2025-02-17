import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = np.random.rand(10)

plt.subplot(221)
plt.bar(x, y, label="rnd")
plt.subplot(222)
plt.plot(x,y, label="plot", color="red")
plt.legend()
plt.show()