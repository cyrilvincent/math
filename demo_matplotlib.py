import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)


plt.subplot(2,2,1)
plt.plot(x, y, color="red", label="courbe1")
plt.subplot(222)
plt.bar(x, y2, color="green", label="courbe2")
plt.legend()
plt.title("Démo")
plt.subplot(223)
plt.scatter(x, y2, color="blue", label="courbe2")
plt.show()